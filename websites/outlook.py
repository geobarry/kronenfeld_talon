from talon import Context,Module,actions,clip
import re
mod = Module()


@mod.action_class
class Actions:
    def outlook_go_to_messages():
        """Navigates outlooks arcane idiosyncratic interface to get to the messages section"""
        # name: New 	class_name: d2l-label-text
        prop_dict = [("OR",[("name","App launcher"),("name","Sort message list by Received")])]
        actions.user.key_to_matching_element("tab",prop_dict)
        actions.sleep(0.3)
        actions.user.slow_key_press("ctrl-y down up")        
ctx = Context()