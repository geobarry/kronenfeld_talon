from talon import Context,Module,actions,clip
import re
mod = Module()


@mod.action_class
class Actions:
    def word_enable_editing():
        """Enables editing in Microsoft word when it opens up in Protected Mode"""
        prop_dict = [("name","Enable Editing")]
        actions.user.invoke_matching_element(prop_dict)
    def word_display_markup(display_option: str):
        """Selects what markup to show when tracking changes"""
        actions.key("alt r z t t d")
        actions.user.key_to_elem_by_val("down",display_option)
        actions.key("enter esc esc")
    def word_go_to_comments():
        """Navigates to the comment pane"""
        prop_dict = ["OR",[
                        ("name","New comment"),
                        ("name","Comment thread.*"),
                        ("name","Like"),
                        ("name","More thread actions"),
                        ("class_name","NetUIElement")
                    ]]
        actions.user.key_to_matching_element("f6",prop_dict,limit = 7)
    def word_go_to_main_text():
        """Navigates to the main text panel"""
        prop_dict = [("name",".*\.docx?$")]
        actions.user.key_to_matching_element("f6",prop_dict,limit = 7)
ctx = Context()