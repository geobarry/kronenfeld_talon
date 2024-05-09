from typing import Tuple
from talon import Context, Module, ctrl, cron, actions, imgui, ui

# parameters
reaction_time = 1500 # set to 0 if you don't want backwards-correction
check_repeat_time = 20 # milliseconds to check to see if it's time to repeat
minimum_repeat_interval = 30 # milliseconds
speed_change = 100 # milliseconds per repeat
opposites = {
    'left': 'right',
    'right': 'left',
    'up': 'down',
    'down': 'up',
    'tab': 'shift-tab',
    'shift-tab': 'tab',
    'f6': 'shift-f6',
    'shift-f6': 'f6'
}
class SlowRepeater:
    def __init__(self):
        self.enabled = False
        self.cumulative_time = 0
    def enable(self, key, ms):
        key_parts = key.split("-")
        self.key = key_parts[-1]
        self.modifier_key = None
        if len(key_parts) > 1:
            self.modifier_key = "-".join(key_parts[:-1])
            actions.key("{}:down".format(self.modifier_key))
        self.ms = ms
        if self.enabled:
            cron.cancel(self.job)
        self.enabled = True
        # check for repeat every 20 milliseconds
        self.job = cron.interval('{}ms'.format(check_repeat_time), self.repeat_command)
    def disable(self):
        if not self.enabled:
            return
        cron.cancel(self.job)
        # undo moves based on reaction time
        if reaction_time > 0:
            if self.key in opposites.keys():
                n = int(min(self.cumulative_time, reaction_time)/self.ms)
                for i in range(n):
                    actions.sleep(self.ms/1000)
                    actions.key(opposites[self.key])
        if self.modifier_key != None:
            actions.sleep(1.5)
            actions.key("{}:up".format(self.modifier_key))
        self.cumulative_time = 0
        self.modifier_key = None
        self.enabled = False

    def repeat_command(self):
        self.cumulative_time += check_repeat_time
        # time to repeat command if modulus remainder < check_repeat_time
        if self.cumulative_time % self.ms < check_repeat_time:
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
        repeater_object.repeat_command()
        gui_repeater.show()
        ctx.tags = ["user.slow_repeating"]

    def stop_repeating():
        """Terminate repetition"""
        gui_repeater.hide()
        repeater_object.disable()
    def hard_stop_repeating():
        """Terminate Immediately"""
        gui_repeater.hide()
        repeater_object.ms = reaction_time + 1
        repeater_object.disable()
    def repeat_faster():
        """Reduce repeat interval"""
        repeater_object.ms = max(repeater_object.ms-speed_change,minimum_repeat_interval)
    def repeat_slower():
        """Increase repeat interval"""
        repeater_object.ms = max(repeater_object.ms+speed_change,minimum_repeat_interval)
        
ctx = Context()
