from talon import Module,Context,actions

mod = Module()

@mod.action_class
class Actions:
    def notepad_promote():
        """dedent current line"""
        actions.edit.select_line()
        actions.key("shift-tab")
    def notepad_demote():
        """indent current line"""
        actions.edit.line_start()
        actions.key("tab")
        
ctx = Context()