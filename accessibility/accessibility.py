from talon import Module, ui, Context, clip, ctrl, cron, actions
from talon.windows import ax as ax
from talon.types import Point2d as Point2d
import inspect
import math
import re

# list for tracking a set of clickable points
loc_marks = []

class mouse_mover:
    """Moves mouse using cron intervals until destination is reached"""
    def __init__(self, dest: Point2d, callback = None):        
        self.callback = callback
        self.dest = dest
        self.orig = ctrl.mouse_pos()
        self.cur = self.orig
        dx = self.dest.x - self.orig[0]
        dy = self.dest.y - self.orig[1]
        totD = ((dx ** 2) + (dy ** 2)) ** 0.5
        totT = self.get_move_time(totD)
        print(f"totD: {totD}  |  totT: {totT}")
        self.num_intervals = max(1,math.ceil(totT / 30))
        self.interval_x = dx / self.num_intervals
        self.interval_y = dy / self.num_intervals
        print(f"dx: {self.interval_x}  |  dy: {self.interval_y}")
        self.job = cron.interval('30ms', self.move_next)
        self.completed = 0

    def get_move_time(self,d):
        """Calculates the total time to move the mouse based on distance in pixels"""
        # Keys: move distance (pixels)
        # Values: move time (ms)
        move_times = {
            -1:50,
            100:200,
            500:350,
            1000:450,
            2000:700,
            10000:1200,
            1000000:100000
        }
        dkeys = sorted(list(move_times))

        d = abs(d)
        id = 0
        while dkeys[id] < d:
            id += 1
        lowD,highD = dkeys[id-1],dkeys[id]
        lowT,highT = move_times[lowD],move_times[highD]
        return int(lowT + (highT - lowT) * (d - lowD) / (highD - lowD))


    def move_next(self):
        """Moves mouse by one interval until destination reached"""
        # handle last move
        if self.completed == self.num_intervals - 1:
            ctrl.mouse_move(self.dest.x,self.dest.y)
            cron.cancel(self.job)
            if self.callback != None:
                self.callback()
        else:
            # handle previous moves
            self.completed += 1
            x = round(self.orig[0] + self.interval_x * self.completed)
            y = round(self.orig[1] + self.interval_y * self.completed)
            ctrl.mouse_move(x,y)

mod = Module()

mod.list("handle_position","position for grabbing ui elements")    


def get_every_child_alias(el: ax.Element):
    # apparently keeping elements in memory is very expensive,
    # would be better to find some way to do what you want with element properties
    if el:
        for child in el.children:
            # filter to see if this is faster
            #if child.is_keyboard_focusable:
            texts = [x for x in [el.name,el.help_text] if x != ""]
            if len(texts) > 0:
                yield " ".join(texts)
            yield from get_every_child_alias(child)


def get_every_child(el: ax.Element):
    # apparently keeping elements in memory is very expensive,
    # would be better to find some way to do what you want with element properties
    if el:
        for child in el.children:
            # filter to see if this is faster
            #if child.is_keyboard_focusable:
            if str(el.name) != "" or str(el.help_text) != "":
                yield child

            yield from get_every_child(child)

def all_element_information(el):
    msg = f'\n\n{el.name}: ' 
    for p,v in vars(el).items():
        msg += f'\n{type(v)}'

    return msg


def element_match(el: ax.Element, prop_list, conjunction="AND"):
    """Returns true if the element matches all of the properties in the property dictionary"""
    # prop_list is either a list of form [(property, trg_val),...]
    #     where trg_val is either a string (for an exact match)
    #     or a regex expression
    # or a list of ["OR",list] or ["AND",list]
    # Conditions in the top level list are connected with an AND conjunction
    def eval_cond(prop,trg_val):
        def value_match(prop_val,trg_val):
            if type(trg_val) == re.Pattern:
                return re.match(trg_val,prop_val) != None
            else:
                return prop_val.lower() == trg_val.lower()
        if prop in ["AND","OR"]:
            return element_match(el,trg_val,prop)
        if prop == "name":
            return value_match(el.name,trg_val)
        if prop == "class_name":
            return value_match(el.class_name,trg_val)
        if prop == "help_text":
            return value_match(el.help_text,trg_val)
        if prop == "clickable":
            clickable = True
            try:
                loc = el.clickable_point
            except:
                clickable = False
            finally:
                return trg_val == clickable
        # if something is not properly specified, return true so that other conditions can be evaluated
        print("ERROR in function element_match (accessibility.py)")
        print("No matching property found (looking for property: {prop})")
        print(prop_list)
        return True
    if prop_list[0] in ["AND","OR"]:
        return element_match(el,prop_list[1],prop_list[0])
    if conjunction == "AND":
        return all([eval_cond(prop,val) for prop,val in prop_list])
    if conjunction == "OR":
        return any([eval_cond(prop,val) for prop,val in prop_list])
    


def element_information(el: ax.Element, verbose = False):
        msg = f"148 name: {el.name} \tclass_name: {el.class_name} \thelp_text: {el.help_text}"
        print(msg)
        try:
            msg += f"\tloc: {el.clickable_point.x},{el.clickable_point.y}"
        except:
            msg += f"\tloc: None"
        if verbose:
            msg += f"\npid: {el.pid}"
            msg += f"\naccess_key: {el.access_key}"
            msg += f"\nhas_keyboard_focus: {el.has_keyboard_focus}"
            msg += f"\nis_keyboard_focusable: {el.is_keyboard_focusable}"
            msg += f"\nis_enabled: {el.is_enabled}"
            msg += f"\nautomation_id: {el.automation_id}"
            msg += f"\nchildren: {len(el.children)}"
            msg += f"\nis_control_element: {el.is_control_element}"
            msg += f"\nis_content_element: {el.is_content_element}"
            msg += f"\nitem_type: {el.item_type}"
            msg += f"\nitem_status: {el.item_status}"
            msg += f"\npatterns: {el.patterns}"
            msg += f"\ndescribed_by: {el.described_by}"
            msg += f"\nflows_to: {el.flows_to}"
            msg += f"\nprovider_description: {el.provider_description}"
            try:
                msg += f"\ncustomnavigation_pattern: {el.customnavigation_pattern}"
            except:
                pass
            try:
                msg += f"\nwindow_pattern: {el.window_pattern}"
            except:
                pass
            try:
                msg += f"\nitemcontainer_pattern: {el.itemcontainer_pattern}"
            except:
                pass
            try:
                msg += f"\nselection_pattern: {el.selection_pattern}"
            except:
                pass
            try:
                msg += f"\nselection_pattern2: {el.selection_pattern2}"
            except:
                pass                
            try:
                msg += f"\ngetting toggle pattern state:"
                toggle_pattern = el.toggle_pattern
                msg += f"\ntoggle_pattern.state: {toggle_pattern.state}"
            except:
                pass
            try:
                msg += f"\nitemcontainer_pattern: {el.itemcontainer_pattern}"
            except:
                pass
            try:
                msg += f"\nrect: {el.rect}"
            except:
                pass

#            msg += "\n\nCHILDREN:"
#            for child in el.children:
#                msg += element_information(child,True)
        return msg

def dynamic_children_experiment(_) -> dict[str,str]:
    root = ui.active_window().element
    aliases = list(get_every_child_alias(root))
    output = {}
    for alias in aliases:
        # add full name to dictionary
        output[alias] = alias
        # add single word command to dictionary
        singles = re.split('[^a-zA-Z]',alias)
        output[singles[0]] = alias
        # add double word command to dictionary
        if len(singles) > 1:
            output[" ".join(singles[:2])] = alias
    return output

        

ctx = Context()

mod.list("dynamic_children", desc="List of children of the active window")

@ctx.dynamic_list("user.dynamic_children")
def dynamic_children(_) -> dict[str,str]:
    root = ui.active_window().element
    elements = list(get_every_child(root))
    out = {}
    for el in elements:
        alias = str(el.name)
        if alias == "":
            alias = str(el.help_text)
        if alias != "":
            # add full name to dictionary
            out[str(el.name)] = str(el.name)
            # add single word command to dictionary
            singles = re.split('[^a-zA-Z]',str(el.name))
            out[singles[0]] = str(el.name)
            # add double word command to dictionary
            if len(singles) > 1:
                out[" ".join(singles[:2])] = str(el.name)
    return out


@mod.action_class
class Actions:

    def element_exists(prop_list: list):
        """Returns true if an element where the given properties exists"""
        root = ui.active_window().element
        elements = list(get_every_child(root))
        for el in elements:
            if element_match(el,prop_list):            
                return True
        return False
        
    def element_list():
        """returns_a_list_of_all_elements"""
        root = ui.active_window().element
        return list(get_every_child(root))

    def element_property_value(property_name: str, sleep_time: float=0.02):
        """returns the value of the given property for the currently focused element"""
        actions.sleep(sleep_time)
        el = ui.focused_element()
        if property_name == "name":
            return el.name
        if property_name == "class_name":
            return el.class_name
        if property_name == "el.help_text":
            return el.help_text

    def peek_next_property_value(property_name: str, key: str="tab", rev_key: str=""):
        """returns the value of the property of the next element and then returns the previous element"""
        reverse_keys = {
            "tab": "shift-tab",
            "right": "left",
            "down": "up",
            "f6": "shift-f6"
        }
        if rev_key == "":
            rev_key = reverse_keys[key]
        actions.key(key)
        val = actions.user.element_property_value(property_name)
        actions.key(rev_key)
        return val
        
    def toggle_for_next_value(trg: str, toggle_key: str, advance_key: str="tab", property_name: str="name"):
        """Toggles current element until the next elements value meets the target value"""
        cur_val = actions.user.peek_next_property_value(property_name,advance_key)
        if cur_val != trg:
            actions.key(toggle_key)
        
    def focus_element_by_name(name: str):
        """Focuses on an element by name"""
        root = ui.active_window().element
        elements = list(get_every_child(root))
        
        for element in elements:
            if element.name == name or \
            str(element.name).lower() == name or \
            name.lower() in str(element.name).lower():
                element.invoke_pattern.invoke()
                break
        else:
            print("Element not found")

    def click_focused(down_key: str=""):
        """ clicks on the currently focused element with the down key pressed"""
        if down_key != "":
            actions.key(f"{down_key}:down")
        el = ui.focused_element()
        try:
            loc = el.clickable_point
            mouse_obj = mouse_mover(loc,ctrl.mouse_click)
        except:
            pass
        if down_key != "":
            actions.key(f"{down_key}:up")

    def mark_focused_location():
        """records the clickable point of the currently focused item"""
        global loc_marks
        el = ui.focused_element()
        try:
            loc_marks.append(el.clickable_point)
        except:
            pass
        print(f"{len(loc_marks)} locations marked!")
        
    def click_all_marks(down_key: str=""):
        """clicks on recorded marks and then empties list"""
        global loc_marks
        i = 0
        for mark in loc_marks:
            if down_key != "":
                actions.key(f"{down_key}:down")
            try:
                ctrl.mouse_move(mark.x,mark.y)
                ctrl.mouse_click()
            except:
                pass
            if down_key != "":
                actions.key(f"{down_key}:up")
            i += 1
        # reset location marks list
        loc_marks = []


    def click_element_by_name(name: str, exact_match: bool = False):
        """Moves mouse to and clicks on element"""
        root = ui.active_window().element
        elements = list(get_every_child(root))
        for el in elements:
            print(el.name)
            if el.name == name or \
                str(el.name).lower() == name or \
                (name.lower() in str(el.name).lower() and not exact_match):
                try:
                    loc = el.clickable_point
                    mouse_obj = mouse_mover(loc,ctrl.mouse_click)
                    break
                except:
                    # if element doesn't have a clickable point, 
                    # see if it has a rectangle
                    try:
                        rect = el.rect
                        x = rect.x + int(rect.width/2)
                        print('x: {x}')
                    except:
                        pass


         

    def click_matching_element(prop_list: list):
        """clicks on the element that matches property dictionary"""
        # make sure that clickable property is set to true
        if not ("clickable",True) in prop_list:
            prop_list.append(("clickable",True))
        # get list of elements
        root = ui.active_window().element
        elements = list(get_every_child(root))
        # search for match
        for el in elements:
            if element_match(el,prop_list):
                loc = el.clickable_point
                mouse_obj = mouse_mover(loc,ctrl.mouse_click)
                break

    def key_to_matching_element(key: str, prop_list: list, limit: int=35, escape_key: str=None):
        """press given key until the first matching element is reached"""
        i = 1
        last_el = element_information(ui.focused_element(),verbose = True)
        el = ui.focused_element()
        msg = f"name: {el.name} \tclass_name: {el.class_name} \thelp_text: {el.help_text}"
        while (not element_match(ui.focused_element(),prop_list)) and (i < limit):            
            actions.key(key)
            if (last_el == element_information(ui.focused_element(),verbose = True)) and (escape_key != None):
                actions.key(escape_key)
            i += 1

    def key_to_elem_by_val(key: str, val: str, prop: str="name", limit: int=35, escape_key: str=None):
        """press key until element with exact value for one property is reached"""
        prop_list = [(prop,val)]
        actions.user.key_to_matching_element(key,prop_list,limit,escape_key)

    def move_to_element(name: str):
        """Moves mouse to element"""
        root = ui.active_window().element
        elements = list(get_every_child(root))
        for element in elements:
            if element.name == name or \
            str(element.name).lower() == name:                
                loc = element.clickable_point
                mouse_obj = mouse_mover(loc)
                break
        else:
            print("Element not found")

    def move_mouse_to_focused_element(pos: str="center", x_offset: int=0, y_offset: int=0):
        """moves mouse to left,right or center and top,bottom or center of currently focused element"""
        el = ui.focused_element()
        try:
            rect = el.rect
            print('rect: {rect} (type: {type(rect)})')
            print(rect.x)
            if "left" in pos:
                x = rect.x
            elif "right" in pos:
                x = rect.x + rect.width
            else:
                x = rect.x + int(rect.width/2)
            if "upper" in pos or "top" in pos:
                y = rect.y
            elif "lower" in pos or "bottom" in pos:
                y = rect.y + rect.height
            else:
                y = rect.y + int(rect.height/2)
            x += x_offset
            y += y_offset
            ctrl.mouse_move(x,y)
        except:
            pass
        


    def copy_elements_accessible_by_key(key: str, limit: int=35):
        """Gets information on elements accessible by pressing the input key"""        
        elements = []
        full_elements = []
        i = 1
        actions.key(key)
        cur_msg = element_information(ui.focused_element(), verbose = False)
        full_msg = element_information(ui.focused_element(), verbose = True)
        while (not full_msg in full_elements) and (i < limit):
            elements.append(cur_msg)
            full_elements.append(full_msg)
            actions.key(key)
            cur_msg = element_information(ui.focused_element(), verbose = False)
            full_msg = element_information(ui.focused_element(), verbose = True)    
            i += 1
        clip.set_text("\n".join(elements))
                

    def copy_near_elements_to_clipboard(max_dist: int=500):
        """Copies elements with valid clickable point within given number of pixels"""
        pos = ctrl.mouse_pos()
        root = ui.active_window().element
        elements = list(get_every_child(root))
        id = 0
        n = 0
        msg = ""        
        for el in elements:
            id += 1
            
            try:
                loc = el.clickable_point
                d = abs(loc.x-pos[0]) + abs(loc.y-pos[1])                
                if d < max_dist:
                    msg += element_information(el) + "\n"
                    n += 1
            except:
                pass
        msg += f"\n\n {n} elements found"
        clip.set_text(msg)

        

    def copy_accessible_elements_to_clipboard():
        """Copies focusable elements to the clipboard"""
        root = ui.active_window().element
        elements = list(get_every_child(root))
        id = 0
        msg = ""
        
        for el in elements:
            id += 1
            msg += f"\n{id}: {el.name}"
#            msg += f"\n{id}: {label} enabled: {el.is_enabled} loc: {el.clickable_point}"
        clip.set_text(msg)
        
    def copy_focused_element_to_clipboard():
        """Copies information about currently focused element to the clipboard"""
        el = ui.focused_element()
        match = element_match(ui.focused_element(),[("class_name","TreeView")])
        msg = element_information(el, verbose = True)
        clip.set_text(msg)
        
    def copy_enabled_element_to_clipboard():
        """Searches for the first enabled element and copies is information to the clipboard"""
        root = ui.active_window().element
        elements = list(get_every_child(root))
        msg = "ENABLED ELEMENT(S)\n"
        for element in elements:
            if element.is_enabled:
                msg += element_information(element) +"\n"
        clip.set_text(msg)
        
    def copy_clickable_element_to_clipboard():
        """Searches for the first enabled element and copies is information to the clipboard"""
        root = ui.active_window().element
        elements = list(get_every_child(root))
        msg = "ENABLED ELEMENT(S)\n"
        for element in elements:
            try:
                x = element.clickable_point
                msg += element_information(element) +"\n"
            except:
                pass 
        clip.set_text(msg)
        
    def copy_keyboard_element_to_clipboard():
        """Searches for elements that have keyboard focus and are clickable
        and copies information to clipboard"""
        root = ui.active_window().element
        elements = list(get_every_child(root))
        msg = "ENABLED ELEMENT(S)\n"
        for element in elements:
            if element.has_keyboard_focus:
                try:
                    x = element.clickable_point
                    msg += element_information(element) +"\n"
                except:
                    pass 
        clip.set_text(msg)

    def test_copy_all():
        """Attempts to retrieve all properties from all elements"""
        root = ui.active_window().element
        elements = list(get_every_child(root))
        elements.append(root)
        msg = ""
        for el in elements:
            msg += element_information(el) + "\n"
        clip.set_text(msg)
        
        
        
        
        
        
        
        
        
        
        