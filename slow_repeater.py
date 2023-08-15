from typing import Tuple
from talon import Context, Module, ctrl, cron, actions
class SlowRepeater:
    def __init__(self):
        self.enabled = False
    def enable(self, key, ms):
        self.key = key
        self.ms = ms
        if self.enabled:
            cron.cancel(self.job)
        self.enabled = True
        self.job = cron.interval('{}ms'.format(self.ms), self.repeat_command)
    def disable(self):
        if not self.enabled:
            return
        cron.cancel(self.job)
        self.enabled = False

    def repeat_command(self):
        actions.key(self.key)

repeater_object = SlowRepeater()
mod = Module()
mod.tag("slow_repeating", desc="In the middle of repeating a task")

@mod.action_class
class Actions:
    def start_repeating(key: str, ms: int):
        """Initiate repetition"""
        repeater_object.enable(key, ms)

    def stop_repeating():
        """Terminate repetition"""
        repeater_object.disable()

ctx = Context()
