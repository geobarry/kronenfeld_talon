from talon import Context,Module,actions,clip
import subprocess
import re
mod = Module()

mod.list("explorer_heading","headings that can be sorted by")

time_last_pop = 0
num_recent_pops = 0

@mod.action_class
class Actions:
    def explorer_open_path_in_terminal():
        "Open path in terminal"
        actions.user.file_explorer_copy_folder()
        process = subprocess.Popen(["cmd.exe"], cwd=clip.text())
        process.returncode = 0
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
        actions.user.key_to_matching_element("tab",[("class_name","UIItem")],limit = 35, escape_key = "esc")
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
    def file_explorer_sort_by(col_name: str):
        """sort files and folders by column"""
        print(col_name)
        actions.user.key_to_matching_element("tab",[("class_name","UIColumnHeader")])
        actions.user.key_to_matching_element("right",[("name",f"{col_name}.*")],limit = 15)
        actions.key("enter")
    def explorer_navigate_to_folder(path: str):
        """navigates to given folder in ff explorer like application or dialog"""
        actions.key("alt-d")
        actions.sleep(0.2)
        actions.insert(path)
        actions.sleep(0.2)
        actions.key("enter")
        # get rid of annoying dropdown suggestions that don't disappear on their own
        actions.sleep(0.5)
        actions.key("alt-d")
        actions.sleep(0.5)
        actions.key("esc tab:2")
        actions.sleep(0.5)
        actions.key("tab:5")
        # returned to file area
        actions.user.file_explorer_tab_to_files()

    
ctx = Context()