from talon import Context,Module,actions,clip
import re
mod = Module()


@mod.action_class
class Actions:
    def outlook_refresh():
        """Refresh all email folders"""
        prop_list = [("automation_id","SendReceiveAll")]
        el = actions.user.matching_elements(prop_list)[0]
        pattern = el.invoke_pattern
        pattern.invoke()
    def outlook_new_email():
        """Start a new email"""
        prop_list = [("automation_id","NewItem")]
        el = actions.user.matching_elements(prop_list)[0]
        pattern = el.invoke_pattern
        pattern.invoke()
    def outlook_attach_file():
        """Attach a file to current email"""
        # Expand the attachment options
        prop_list = [("automation_id","AttachFileSplit")]
        el = actions.user.matching_elements(prop_list)[0]
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
        prop_list = [("name",".*attachments"),("class_name","NetUISimpleButton")]
        el = actions.user.matching_element(prop_list)
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
        el = actions.user.matching_element(prop_list)
        el.invoke_pattern.invoke()        
ctx = Context()