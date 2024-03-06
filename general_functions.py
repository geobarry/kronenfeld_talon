from talon import Context,Module,actions
import time
mod = Module()

time_last_pop = 0
num_recent_pops = 0

@mod.action_class
class Actions:
    def slow_key_press(key_seq: str, wait_time: float=0.1, flag: str=""):
        """Press a sequence of keys separated by spaces slowly"""
        key_strings = key_seq.split(" ")
        def press_key(key):
            actions.key(key)
            if wait_time > 0:
                actions.sleep(wait_time)
        for key in key_strings:
            if ":" in key:
                parts = key.split(":")
                if parts[1].isnumeric():                    
                    for id in range(int(parts[1])):
                        press_key(parts[0])
                else:
                    press_key(key)
            else:
                press_key(key)
            if flag == "one_delay_only":
                wait_time = 0
    def compress_video_file():
        """Compresses the video file that is currently selected in windows file explorer"""
        actions.key("f2")
        actions.sleep(0.2)
        orig_file_name = actions.edit.selected_text()
        new_file = orig_file_name[:]
        new_file = new_file.replace(" ","_")
        mod_file_name = f"{new_file}_full"
        print(mod_file_name)
        actions.sleep(0.2)
        actions.insert(mod_file_name)
        actions.sleep(0.2)
        actions.key("enter")
        actions.sleep(0.2)
        actions.key("alt-d")
        actions.sleep(0.2)
        folder_path = actions.edit.selected_text()
        actions.sleep(0.2)
        actions.key("esc")
        actions.sleep(0.2)
        actions.key("tab:2")
        print("FOLDER PATH")
        print(folder_path)
        new_file = f"{new_file}.mp4"
        orig_file = f"{mod_file_name}.mp4"
        command = f"ffmpeg -i {orig_file} -c:v libx264 -c:a aac {new_file}"
        # print(command)
        actions.sleep(0.1)
        actions.key("super")
        actions.sleep(0.5)
        actions.insert("command prompt")
        actions.sleep(0.5)
        actions.key("enter")
        actions.sleep(1.5)
        actions.insert(f"cd {folder_path}")
        actions.sleep(1)
        actions.key("enter")
        actions.insert(command)
    def mute_zoom_on_double_pop():
        """Looks for two pops in a row in order to mute Zoom"""
        global time_last_pop
        global num_recent_pops
        delta = time.time() - time_last_pop
        time_last_pop = time.time()
        
        if delta > 0.5:
            num_recent_pops = 1
        else:
            num_recent_pops += 1
        
        print(f"delta: {delta} num_pops: {num_recent_pops}")
        
        if num_recent_pops == 2:
            print("got exactly two pops")
            actions.speech.enable()
            actions.key("alt-a")
    def mute_teams_on_double_pop():
        """Looks for two pops in a row in order to mute Teams"""
        print(f"mute_teams_on_double_pop: FUNCTION START")
        global time_last_pop
        global num_recent_pops
        delta = time.time() - time_last_pop
        time_last_pop = time.time()
        
        if delta > 0.5:
            num_recent_pops = 1
        else:
            num_recent_pops += 1
        
        print(f"delta: {delta} num_pops: {num_recent_pops}")
        
        if num_recent_pops == 2:
            print("got exactly two pops")
            actions.speech.enable()
            actions.key("ctrl-shift-m")
        
ctx = Context()
