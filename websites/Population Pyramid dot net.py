from talon import Context,Module,actions,clip
import re
mod = Module()


@mod.action_class
class Actions:
    def populationpyramid_letter_countries(letter: str):
        """Goes to countries by letter"""        
        prop_dict = [("name",f"{letter.upper()}$")]
        actions.user.key_to_matching_element("tab",prop_dict,999)
        actions.user.key("enter")
ctx = Context()