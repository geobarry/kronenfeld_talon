from talon import Context,Module,actions,clip
import re
mod = Module()


@mod.action_class
class Actions:
    def pdf_button(name: str):
        """Press a PDF button in edge browser """
        prop_list = [("name",name),("help_text",name)]
        actions.user.click_matching_element(prop_list)
        print("what's wrong with this?")
ctx = Context()