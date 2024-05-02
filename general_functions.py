from talon import Context,Module,actions,clip
import time
import re
mod = Module()

time_last_pop = 0
num_recent_pops = 0
dummy = True

@mod.capture(rule="<number> point <number>|<number>")
def real_number(m) -> float:
    """a spoken float"""
    print("CAPTURE: real_number")
    print(type(m))
    
    if len(m) == 1:
        return float(m[0])
    else:
        return float(m[0]) + float(m[2]/(10**len(str(m[2]))))

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
            print(key)
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
    def office_keys(key_seq: str):
        """Convenience function for accessing office menus"""
        # Delay second keypress only
        actions.user.slow_key_press(key_seq, wait_time = 0.2, flag = "one_delay_only")
    def make_clipboard_one_line(sep: str = " "):
        """removes line breaks and then pastes"""
        
        x = clip.text()
        x = re.split(pattern="(\n|\r)+",string = x)
        x = [y.strip() for y in x]
        x = [y for y in x if y != '']
        print(x)
        x = sep.join(x)
        print(x)
        clip.set_text(x)        
                
        
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
    
    def insert_nth_word(text: str, n: int = 0, sep: str = " "):
        """Inserts the nth word in the given string, as defined by the separator"""
#        actions.insert(text.split(sep)[n])
        return text.split(sep)[n]
ctx = Context()
