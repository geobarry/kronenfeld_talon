from talon import Context,Module,actions,clip,ui
from talon.windows import ax as ax
import re
mod = Module()

mod.list("outlook_folder","folders in which email messages are stored in Microsoft outlook 365")

@mod.action_class
class Actions:
    def outlook_go_to_messages():
        """Navigates outlooks arcane idiosyncratic interface to get to the messages section"""
        # Determine if we are in search results or not
        prop_dict = [("help_text","All results")]
        if actions.user.element_exists(prop_dict):
            print("SEARCH RESULTS")
            prop_dict = [("name","All results"),("help_text","All results")]
            if actions.user.element_exists(prop_dict):
                print("has results")
                actions.user.click_matching_element(prop_dict)
                actions.sleep(0.1)
                actions.user.click_matching_element(prop_dict)
                actions.sleep(0.1)
                actions.key("down")
        else:
            print("INBOX")
            # first make sure focus is on page content
            actions.key("ctrl-f6")
            # then use random keyboard shortcut to get to messages
            actions.user.slow_key_press("ctrl-y down up",0.25) 
    def outlook_go_to_search():
        """Navigates to the search bar"""
        #prop_dict = [("name","Mail"),("class_name","fui-Button.*")]
        #actions.user.click_matching_element(prop_dict,5)
        #actions.sleep(0.1)
        actions.key("ctrl-f6")
        prop_dict = [("name","Search for email.*")]
        actions.user.key_to_matching_element("shift-tab",prop_dict)
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
    def outlook_go_to_folders():
        """Navigates to and opens the folders section"""
        prop_list = [("name","^Folders$")]
        actions.user.click_matching_element(prop_list,50)
        el = actions.user.matching_elements(prop_list)[0]
        pattern = el.expandcollapse_pattern
        pattern.expand()
    def outlook_go_to_folder(folder_name: str):
        """Navigates Outlook to open the inbox, drafts, junk and other named folders"""
        actions.user.outlook_go_to_folders()
        prop_list = [("name",f"^{folder_name}.*")]
        actions.sleep(0.2)
        actions.user.key_to_matching_element("down",prop_list)
        actions.key("enter")
    def outlook_click_button(command: str):
        """Runs a command on the message command bar"""
        prop_list = [("name",command),("class_name","ms-Button.*root-.*")]
        actions.user.click_matching_element(prop_list)
        
ctx = Context()