from talon import Context,Module,actions
from os import listdir, rename
mod = Module()

@mod.action_class
class Actions:
    def process_desire_to_learn_downloads():
        """trims ALL file names in current folder assuming these have been downloaded from D2L"""
		# get current folder
        actions.key("alt-d")
        path = actions.edit.selected_text()
        for filename in listdir(path):
            old_full_path = "{}\\{}".format(path,filename)
            file_parts = filename.split("-")
            # make sure file names have 5 parts: 
            # 0-1: number codes
            # 2: student name
            # 3: date
            # 4: student-defined-file-name
            if len(file_parts) == 5:
                short_date = file_parts[3].split(",")[0]
                # make sure short date begins with a month
                if short_date[0:3] in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]:
                    new_file = "{}-{}-{}".format(file_parts[2],short_date,file_parts[4])
                    new_full_path =  "{}\\{}".format(path,new_file)
                    rename(old_full_path,new_full_path)
ctx = Context()