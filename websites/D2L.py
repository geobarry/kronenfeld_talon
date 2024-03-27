from talon import Context,Module,actions,clip
import re
mod = Module()


@mod.action_class
class Actions:
    def D2L_add_new_file_from_computer():
        """Adds a file to a content section"""
        # name: New 	class_name: d2l-label-text
        prop_dict = {"name":"New","class_name":"d2l-label-text"}
        actions.user.click_matching_element(prop_dict)
        actions.sleep(1)
        actions.key("tab enter")
        actions.sleep(0.75)
        actions.key("tab shift-tab enter")
        actions.sleep(0.75)
        actions.key("tab:3")
        actions.sleep(0.5)
        actions.key("enter")
        
ctx = Context()