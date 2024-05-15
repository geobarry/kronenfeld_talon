# Python module to activate tag to indicate that we are currently recording in powerpoint
# Is this really necessary, or can this be done using only talon files???
from talon import Context, Module, screen, ui, ctrl, actions
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
    def power_select_full_screen():
        """Selects the entire screen after powerpoint is already in screen recording selection mode"""
        screen = ui.main_screen()
        actions.user.slow_mouse(0,screen.height-1,900)
        actions.sleep(1)
        actions.user.mouse_drag(0)
        actions.sleep(0.4)
        actions.user.slow_mouse(screen.width-1,1,900)
        actions.sleep(1)
        actions.user.mouse_drag_end()

ctx = Context()

