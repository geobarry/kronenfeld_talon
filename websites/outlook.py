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
    def outlook_go_to_search():
        """Navigates to the search bar"""
        prop_dict = [("name","Search for email.*")]
        actions.user.key_to_matching_element("tab",prop_dict)
    def outlook_go_to_attachment():
        """Navigates to the first attachment it finds"""
        prop_dict = [("name","More actions.*"),("class_name","ms-Button.*--icon")]
        actions.user.key_to_matching_element("tab",prop_dict)
#        actions.sleep(0.3)
        actions.key("enter")
    def outlook_go_to_unread():
        """Navigates Outlook to get to the next unread message"""
        prop_dict = [("name","Unread.*")]
        actions.user.select_matching_element(prop_dict)
        actions.key("down up")
    def outlook_go_to_inbox():
        """Navigates Outlook to open the inbox"""
        prop_list = [("name","^Folders$")]
        actions.user.click_matching_element(prop_list,50)
        actions.sleep(0.1)
        actions.user.click_matching_element(prop_list,50)
        actions.sleep(0.2)
        actions.key("down enter")
    def outlook_click_button(command: str):
        """Runs a command on the message command bar"""
        prop_list = [("name",command),("class_name","ms-Button.*root-.*")]
        actions.user.click_matching_element(prop_list)
        
ctx = Context()