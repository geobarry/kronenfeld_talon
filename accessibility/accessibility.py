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


def element_match(el: ax.Element, prop_dict):
    """Returns true if the element matches all of the properties in the property dictionary"""
    for prop in prop_dict.keys():
        if prop == "name":
            if el.name != prop_dict[prop]:
                return False
        if prop == "class_name":
            if el.class_name != prop_dict[prop]:
                return False
        if prop == "help_text":
            if el.help_text != prop_dict[prop]:
                return False
        if prop == "clickable":
            clickable = True
            try:
                loc = el.clickable_point
            except:
                clickable = False
            if prop_dict[prop] != clickable:
                return False
    return True

def element_information(el: ax.Element, verbose = False):
        msg = f"name: {el.name} \tclass_name: {el.class_name} \thelp_text: {el.help_text}"
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
    def element_exists(prop_dict: dict):
        """Returns true if an element where the given properties exists"""
        root = ui.active_window().element
        elements = list(get_every_child(root))
        for el in elements:
            if element_match(el,prop_dict):            
                return True
        return False
        
    def element_list():
        """returns_a_list_of_all_elements"""
        root = ui.active_window().element
        return list(get_every_child(root))
        
    def focus_element_by_name(name: str):
        """Focuses on an element by name"""
        root = ui.active_window().element
        elements = list(get_every_child(root))
        
        for element in elements:
#            print(element.name)
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
            print(f"current: {el.name}    search: {name}")
            if el.name == name or \
                str(el.name).lower() == name or \
                (name.lower() in str(el.name).lower() and not exact_match):
                try:
                    loc = el.clickable_point
                    mouse_obj = mouse_mover(loc,ctrl.mouse_click)
                    break
                except:
                    pass
        else:
            print("Element not found")

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
         

    def test_copy_all():
        """Attempts to retrieve all properties from all elements"""
        root = ui.active_window().element
        elements = list(get_every_child(root))
        elements.append(root)
        msg = ""
        for el in elements:
            msg += element_information(el) + "\n"
        clip.set_text(msg)

    def click_matching_element(prop_dict: dict):
        """clicks on the element that matches property dictionary"""
        # make sure that clickable property is set to true
        prop_dict["clickable"] = True
        # get list of elements
        root = ui.active_window().element
        elements = list(get_every_child(root))
        # search for match
        for el in elements:
            if element_match(el,prop_dict):
                loc = el.clickable_point
                mouse_obj = mouse_mover(loc,ctrl.mouse_click)
                break

    def key_to_matching_element(key: str, prop_dict: dict, limit: int=35, escape_key: str=None):
        """press is given key until the first matching element is reached"""
        i = 1
        last_el = element_information(ui.focused_element(),verbose = True)
        while (not element_match(ui.focused_element(),prop_dict)) and (i < limit):
            actions.key(key)
            if (last_el == element_information(ui.focused_element(),verbose = True)) and (escape_key != None):
                print("Attempting escape...")
                actions.key(escape_key)
            i += 1

    def copy_elements_accessible_by_key(key: str, limit: int=35):
        """Gets information on elements accessible by pressing the input key"""
        msg = element_information(ui.focused_element(), verbose = False)
        elements = [msg]
        i = 1
        actions.key(key)
        cur_msg = element_information(ui.focused_element(), verbose = False)
        while (not cur_msg in elements) and (i < limit):
            elements.append(cur_msg)
            actions.key(key)
            cur_msg = element_information(ui.focused_element(), verbose = False)
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
                
                print(f"pos: {pos} ({type(pos)})")
                print(f"loc: {loc} ({type(loc)})")
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

        
        
        
        
        
        
        
        
        
        
        