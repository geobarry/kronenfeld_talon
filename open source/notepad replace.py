from talon import Module,Context,actions
mod = Module()
mod.list("notepad_replace_command","commands that can be invoked from notepad replace window")
@mod.action_class
class Actions:
    def notepad_replace_action(command: str):
        """Invokes a command from the notepad++ Replace dialog"""
        prop_list = [("name",f"{command}.*")]
        el = actions.user.matching_element(prop_list)
        el.invoke_pattern.invoke()
ctx = Context()