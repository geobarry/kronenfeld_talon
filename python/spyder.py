from talon import Context,Module,actions,clip,ui,ctrl
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
            r.append(part)
            part = name[i]
        else:
            part += name[i]
    r.append(part)
    return r

@mod.action_class
class Actions:  
    def spyder_focus_panel(panel_name: str):
        """focuses on a panel in spyder"""
        # panel_name is actually a name and a keyboard shortcut, 
        # so we need to first extract the name
        panel_name = panel_name.split(",")[0]
        print(f"function spyder_focus_panel: {panel_name}")
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
# NOTE
# To ensure robustness and maintainability, 
# need to create standard helper functions to: 
# - capture all rows in a panel grid element
# - navigate to a specific grid row
    def spyder_capture_module_names():
        """Navigates project tree to capture module names"""
        # focus on the project panel
        actions.user.spyder_focus_panel("Project")
        el = ui.focused_element()   
        # get python files from grid pattern
        pattern = el.grid_pattern
        messages = []
        for row in range(pattern.row_count):
            if pattern.get_item(row,2).name == "py File":
                filename = str(pattern.get_item(row,0).name[:-3])
                file_parts = split_name(filename)
                if len(file_parts) > 1:
                    filename = " ".join(file_parts) + ":" + filename
                # if "_" in filename:
                    # filename = filename.replace("_"," ") + ":" + filename
                messages.append(filename)
        clip.set_text("\n".join(messages))        
    def spyder_capture_function_names():
        """Navigates outline tree to capture module names"""
        # focus on the outline panel
        actions.user.spyder_focus_panel("Outline")
        el = ui.focused_element()   
        # get python files from grid pattern
        pattern = el.grid_pattern
        messages = []
        for row in range(pattern.row_count):
            func_name = str(pattern.get_item(row,0).name)
            if not func_name[-3:] == ".py":
                parts = split_name(func_name)
                if len(parts) > 1:
                    func_name = " ".join(parts) + ":" + func_name
                messages.append(func_name)
        clip.set_text("\n".join(messages))
    def spyder_test_open_module():
        """test"""
        # focus on the project panel
        actions.user.spyder_focus_panel("Project")
        el = ui.focused_element()   
        el = el.children[3]
        print(f"element name: {el.name}")
        msg = actions.user.element_information(el,headers = True)
        msg += "\n" + actions.user.element_information(el)
        clip.set_text(msg)
        # get python files from grid pattern
        # el = ui.focused_element()
        # pattern = el.grid_pattern
        # messages = [actions.user.element_information(el,headers = True)]
        # for col in range(pattern.column_count):
            # el = pattern.get_item(3,col)
            # actions.user.select_element(el)
            # messages.append(actions.user.element_information(el))
        # row = el.table_pattern.row_header(3)
        # actions.key("enter")
        # clip.set_text("\n".join(messages))
    def spyder_open_module(mod_name: str):
        """Opens the module in the code editor"""
        # first open the project panel
        actions.user.spyder_focus_panel("Project")
        # get children of current element
        el = ui.focused_element()
        r = ''
        # make sure we are at the top
        for i in range(len(el.children)):
            actions.key("up")
        # There's no easy way to do this so we are going to go in parallel
        # looping through element children while also pressing down key
        for child in el.children:
            if child.name[:-3] == mod_name:
                msg = actions.user.element_information(child)
                clip.set_text(msg)
                child.invoke_pattern.invoke()
                break
            # go down one module
            actions.key("down")
        # press entered to open the module
        actions.key("enter")
    def spyder_go_to_function(func_name: str):
        """Opens the function in the code editor"""
        # first open the project panel
        actions.user.spyder_focus_panel("Outline")
        # get children of current element
        el = ui.focused_element()
        r = ''
        # make sure we are at the top
        for i in range(len(el.children)):
            actions.key("up")
        actions.key("down")
        actions.sleep(0.2)
        children = [str(x) for x in el.children]
        # make sure we've gotten everything
        actions.user.mouse_scroll_down()
        actions.sleep(0.2)
        next_children = [str(x) for x in el.children]
        while not next_children[-1] in children:
            print(f'children: {children}')
            print(f'next_children: {next_children}')
            pos = next_children.index(children[-1]) + 1
            children += next_children[pos:]
            next_children = [str(x) for x in el.children]
            actions.user.mouse_scroll_down
            actions.sleep(0.2)
    
        # There's no easy way to do this so we are going to go in parallel
        # looping through element children while also pressing down key
        print(f"elem: {el.name}")
        for child in children:
            actions.sleep(0.2)
            if child == func_name:
                msg = actions.user.element_information(child)
                clip.set_text(msg)
#                child.invoke_pattern.invoke()
                break
            # go down one module
            actions.key("down")
        # press entered to open the module
        actions.key("enter")
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
ctx = Context()