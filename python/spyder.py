from talon import Context,Module,actions,clip,ui,ctrl,screen
from talon.windows import ax as ax
import re
mod = Module()

mod.list("spyder_panel","Panels  in the spyder application")

def split_name(name):
    r = []
    part = name[0]
    for i in range(1,len(name)):
        if name[i] == "_":
            r.append(part)
            part = ""
        elif name[i].isupper():
            # split if previous character is lowercase1
            if name[i - 1].islower():
                r.append(part)
                part = name[i]
            # split if next character is lowercase
            elif i < len(name) - 1:
                if name[i + 1].islower():
                    r.append(part)
                    part = name[i]
            # otherwise don't split
            part += name[i]
        else:
            part += name[i]
    r.append(part)
    return r

def create_talon_list_entry(text):
    """Creates a talon list by getting rid of underscores and separating camel case"""
    parts = split_name(text)
    if len(parts) > 1:
        return " ".join(parts) + ":" + text
    else:
        return text

def get_child_names(panel_name):
    """returns a list of names of children"""
    actions.user.spyder_focus_panel(panel_name)
    pattern = ui.focused_element().grid_pattern
    children = [str(pattern.get_item(row,0).name) for row in range(pattern.row_count)]
    return children

@mod.action_class
class Actions:  
    def spyder_focus_panel(panel_value: str):
        """focuses on a panel in spyder"""
        # extract name from value, which is coming from a talon-list
        panel_name = panel_value.split(",")[0]
        # click on the panel tab
        prop_list = [("name",f"{panel_name}$"),("class_name","$")]
        el = actions.user.matching_elements(prop_list)[0]
        actions.user.click_element(el)
        actions.sleep(0.2)
        # click just above the far right of the QTabBar element
        prop_list = [("class_name","QTabBar")]
        el = actions.user.matching_elements(prop_list)[0]
        r = actions.user.el_prop_val(el,"rect")
        bf = 10
        x = r.x + r.width - bf
        y = max(r.y - bf,bf)
        ctrl.mouse_move(x,y)
        actions.sleep(0.2)
        ctrl.mouse_click()
    def spyder_close_panel(panel_name: str):
        """focuses on a panel and then closes it"""
        actions.user.spyder_focus_panel(panel_name)
        actions.key("ctrl-shift-f4")
    def spyder_open_panel(panel_name: str):
        """Opens the panel and then focuses on it"""
        k = panel_name.split(',')[1].strip()
        k = f"ctrl-shift-{k}"
        print(f'key: {k}')
        actions.key(k)
        actions.user.spyder_focus_panel(panel_name)
    def spyder_capture_module_names():
        """Navigates project tree to capture module names"""
        children = get_child_names("Project")
        mod_names = [create_talon_list_entry(x[:-3]) for x in children if x[-3:] == ".py"]
        clip.set_text("\n".join(mod_names))
    def spyder_capture_function_names():
        """Navigates outline tree to capture module names"""
        children = get_child_names("Outline")
        func_names = [create_talon_list_entry(x) for x in children if x[-3:] != ".py"]
        clip.set_text("\n".join(func_names))
    def spyder_open_module(mod_name: str):
        """Opens the module in the code editor"""
        children = get_child_names("Project")
        [actions.key("up") for child in children]            
        pos = children.index(mod_name + ".py")
        actions.key(f"down:{pos} enter")
    def spyder_go_to_function(func_name: str):
        """Opens the function in the code editor"""
        children = get_child_names("Outline")
        [actions.key("up") for child in children]            
        pos = children.index(func_name)
        actions.key(f"down:{pos} enter")
    def spyder_select_lines(start: int,end: int):
        """Selects the line range"""
        if start > end:
            start,end = end,start
        # go to first line
        actions.key("esc ctrl-l")
        actions.sleep(0.1)
        actions.insert(f"{start}")
        actions.key('enter')
        # select first line
        actions.sleep(0.1)
        actions.edit.extend_line_end()
        # select subsequent lines
        for i in range(end - start):
            actions.edit.extend_line_down()
        actions.edit.extend_line_end()
    def spyder_move_split(direction: str, distance: int = 0):
        """moves splitter to the right of the code panel"""
        prop_list = [("name","Editor"),("class_name","SpyderDockWidget")]
        el = actions.user.matching_element(prop_list)
        x = el.rect.x + el.rect.width + 10
        y = el.rect.y + int(el.rect.height/2)        
        actions.user.slow_mouse(x,y,100)
        actions.sleep(0.2)
        if direction == "left":
            actions.user.eagle_set_bearing(270)
            dx = -1 * distance
        else:
            actions.user.eagle_set_bearing(90)
            dx = distance
        if distance > 0:
            screen = ui.main_screen()
            actions.user.mouse_drag(0)
            actions.sleep(0.1)
            x += dx
            x = max(0,min(x,screen.width - 1))
            print(f'x: {x}')
            actions.user.slow_mouse(x,y,200)
            actions.sleep(0.3)
            actions.user.mouse_drag_end()
ctx = Context()