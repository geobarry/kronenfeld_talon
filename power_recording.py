# Python module to activate tag to indicate that we are currently recording in powerpoint
# Is this really necessary, or can this be done using only talon files???
from talon import Context, Module
mod = Module()
mod.tag("power_recording", desc="Recording a powerpoint slide")
mod.tag("power_screen_recording", desc="Recording screen for a powerpoint slide")
@mod.action_class
class Actions:
    def activate_power_recording():
        """Activate power_recording tag"""
        ctx.tags = ["user.power_recording"]
    def deactivate_power_recording():
        """DeActivate power_recording tag"""
        ctx.tags = []
    def activate_power_screen_recording():
        """Activate power_screen_recording tag"""
        ctx.tags = ["user.power_screen_recording"]
    def deactivate_power_screen_recording():
        """DeActivate power_screen_recording tag"""
        ctx.tags = []

ctx = Context()

