from talon import Context,Module,actions,clip
import re
mod = Module()

time_last_pop = 0
num_recent_pops = 0

@mod.action_class
class Actions:
    def replace_with_underscores():
        """Replaces any odd characters in currently selected file name with underscore"""
        actions.key("f2 ctrl-a")
        actions.sleep(0.3)
        x = actions.edit.selected_text()
        chars = " +?!'\"#"
        for i in range(len(chars)):
            x = x.replace(chars[i],"_")
        print(f"FUNCTION replace_with_underscores: {x}")
        actions.insert(x)
    def file_explorer_tab_to_files():
        """presses the tab key to get to the file list area"""
        actions.user.key_to_matching_element("tab",{"class_name":"UIItem"},escape_key = "esc")
    def file_explorer_copy_folder():
        """Copies the folder path to the clipboard"""
        actions.key("esc ctrl-l")
        actions.sleep(0.2)
        folder = actions.edit.selected_text()
        clip.set_text(folder)
        actions.key("esc")
        actions.sleep(0.2)
        actions.key("tab:5")

    def file_explorer_copy_full_path():
        """Copies the full path of the currently selected file to the clipboard"""
        actions.key("f2 ctrl-a")
        actions.sleep(0.2)
        filename = actions.edit.selected_text()
        actions.key("esc ctrl-l")
        actions.sleep(0.2)
        folder = actions.edit.selected_text()
        clip.set_text(f"{folder}\\{filename}")
        actions.key("esc")
        actions.sleep(0.2)
        actions.key("tab:5")

ctx = Context()