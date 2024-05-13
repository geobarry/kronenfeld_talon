from talon import Context,Module,actions,ui
mod = Module()

@mod.action_class
class Actions:
    def office_enable_editing():
        """Enables editing in Microsoft word when it opens up in Protected Mode"""
        prop_dict = [("name","Enable Editing")]
        actions.user.invoke_matching_element(prop_dict)
    def close_recovery_panel():
        """Navigates to the recovery panel"""
        prop_list = [("name", "Close"),("class_name","NetUIButton")]
        el = actions.user.matching_element(prop_list)
        el.invoke_pattern.invoke()
ctx = Context()