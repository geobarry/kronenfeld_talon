from talon import Context,Module,actions,clip
import re
mod = Module()

mod.list("email_account","Email accounts to access using outlook at least")
mod.list("email_folder","Folders shown in outlook for any email account")

cur_email = ""

@mod.action_class
class Actions:
    def outlook_open_account(acct_name: str, folder: str = "Inbox.*"):
        """Open an email account and go to the inbox"""
        # first collapse all folders except designated account
        prop_list = [("class_name","NetUIWBTreeDisplayNode")]
        elements = actions.user.matching_elements(prop_list)
        prop_list = [("name",f"^{acct_name}$"),("class_name","NetUIWBTreeDisplayNode")]
        try:
            for el in elements:
                if not actions.user.element_match(el,prop_list):
                    if el.expandcollapse_pattern.state == "Expanded":
                        el.expandcollapse_pattern.collapse()
        except:
            pass
    
        # select the account and expand it
        actions.sleep(0.3)
        el = actions.user.matching_element(prop_list)
        try:
            if el.expandcollapse_pattern.state == "Collapsed":
                el.expandcollapse_pattern.expand()
        except:
            pass
            
        # select the folder
        actions.sleep(0.4)
        prop_list = [("name",f"{folder}.*")]
        el = [child for child in el.children if actions.user.element_match(child,prop_list)][0]
        actions.user.select_element(el)
#        actions.key("up down")
    def outlook_refresh():
        """Refresh all email folders"""
        prop_list = [("automation_id","SendReceiveAll")]
        el = actions.user.matching_elements(prop_list)[0]
        pattern = el.invoke_pattern
        pattern.invoke()
    def outlook_new_email():
        """Start a new email"""
        prop_list = [("automation_id","NewItem")]
        el = actions.user.matching_element(prop_list,max_level = 11)
        pattern = el.invoke_pattern
        pattern.invoke()
    def outlook_attach_file():
        """Attach a file to current email"""
        # Expand the attachment options
        prop_list = [("automation_id","AttachFileSplit")]
        el = actions.user.matching_element(prop_list,max_level = 10)
        pattern = el.expandcollapse_pattern
        pattern.expand()
        actions.sleep(0.1)
        # Select the attach items button
        prop_list = [("name","Browse This PC...*"),("class_name","NetUITWBtnMenuItem.*")]
        el = actions.user.key_to_matching_element("down",prop_list)
        if el:
            pattern = el.invoke_pattern
            pattern.invoke()
    def outlook_select_attachment():
        """Selects attachment"""
        prop_list = [("class_name","NetUIAttachmentItemButton")]
        actions.user.key_to_matching_element("tab",prop_list)
    def outlook_send_message():
        """Send current message"""
        prop_list = [("name","Send"),("class_name","Button"),("automation_id","4256")]
        el = actions.user.matching_elements(prop_list)[0]
        # highlight element for a second to confirm action_class
        if el:
            actions.user.highlight_element(el)
            actions.sleep(1.5)
            actions.user.remove_highlight(el)
            el.invoke_pattern.invoke()
    def outlook_close_notifications():
        """Closes the annoying notifications panel"""
        prop_list = [("name","Notifications"),("class_name","NetUIRibbonButton")]
        el = actions.user.matching_element(prop_list)
        el.toggle_pattern.toggle()
        # still in progress - select and toggle don't seem to work
    def outlook_download_attachment():
        """Download the attachment (assuming only one)"""
        print("OUTLOOK DOWNLOAD ATTACHMENT")
        prop_list = [("name",".*attachments"),("class_name","NetUISimpleButton")]
        el = actions.user.matching_element(prop_list)
        print(f"OUTLOOK DOWNLOAD ATTACHMENT: {el.name}")
        el.invoke_pattern.invoke()

        prop_list = [("automation_id","SaveAttachAs")]
        el = actions.user.matching_element(prop_list)
        el.invoke_pattern.invoke()
    def outlook_show_message():
        """returns to message (e.g. from attachment)"""
        prop_list = [("automation_id","ShowMessage")]
        el = actions.user.matching_element(prop_list)
        el.invoke_pattern.invoke()
    def outlook_invoke_by_automation_id(id: str):
        """simply invokes an element"""
        prop_list = [("automation_id",id)]
        el = actions.user.matching_element(prop_list,max_level = 12)
        el.invoke_pattern.invoke()        
ctx = Context()