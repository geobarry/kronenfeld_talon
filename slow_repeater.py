from typing import Tuple
from talon import Context, Module, ctrl, cron, actions, imgui, ui
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

@imgui.open(x=700, y=0)
def gui_repeater(gui: imgui.GUI):
    gui.text(f"Repeating: {repeater_object.key}")
    gui.line()
    if gui.button("Stop repeating [stop repeating]"):
        actions.user.stop_repeating()
        
@mod.action_class
class Actions:
    def start_repeating(key: str, ms: int):
        """Initiate repetition"""
        repeater_object.enable(key, ms)
        gui_repeater.show()

    def stop_repeating():
        """Terminate repetition"""
        repeater_object.disable()
        gui_repeater.hide()

ctx = Context()
