from talon import Module, ui, Context, clip, ctrl, cron, actions, canvas, screen, ui
from talon.windows import ax as ax
from talon.types import Point2d as Point2d
from talon.skia import  Paint
import inspect
import math
import re

# list for tracking a set of clickable points
marked_elements = []

class element_highlights:
    def __init__(self):        
        self.canvas = canvas.Canvas.from_screen(ui.main_screen())
        self.canvas.register('draw', self.draw_canvas) 
        self.canvas.freeze() # uncomment this line for debugging
        self.rectangles = []

    def add_element(self,rect):
        self.rectangles.append(rect)
        print(f"There are now {len(self.rectangles)} elements in highlight list")
        self.canvas.move(0,0) # this forces canvas redraw

    def clear_elements(self):
        self.rectangles = []
        self.canvas.move(0,0) # this forces canvas redraw

    def draw_canvas(self, canvas):
        paint = canvas.paint
        paint.antialias = True
        paint.color = 'f3f'
        paint.style = paint.Style.STROKE
        paint.stroke_width = 7
        paint.dither = True
        print(f"attempting to draw {len(self.rectangles)} elements")
        for rect in self.rectangles:
            canvas.draw_round_rect(rect,25,25,paint)

        
    def disable(self):
        self.canvas.close()
        self.canvas = None

el_highlights = element_highlights()


class mouse_mover:
    """Moves mouse using cron intervals until destination is reached"""
    def __init__(self, dest: Point2d, ms = None, callback = None):        
        self.callback = callback
        self.dest = dest
        self.orig = ctrl.mouse_pos()
        self.cur = self.orig
        dx = self.dest.x - self.orig[0]
        dy = self.dest.y - self.orig[1]
        totD = ((dx ** 2) + (dy ** 2)) ** 0.5
        if ms != None:
            print("milliseconds is it!")
            totT = ms
        else:
            print("have to calculate MillyMilly")
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
        if self.completed >= self.num_intervals - 1:
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
    #     where trg_val is either a string (for case-insensitive match at start of string)
    #     or a regex expression
    # or a list of ["OR",list] or ["AND",list]
    # or just a string, in which case property will be "name"
    # Conditions in the top level list are connected with an AND conjunction
    def eval_cond(prop,trg_val):
        def value_match(prop_val,trg_val):
            if el.name == "All results" or el.name == "Top results":
                print(f"prop_val: {prop_val}, trg_val: {trg_val}")
            # if trg_val is a string, convert to a regex pa'ttern
            if type(trg_val) == str:
                trg_val = re.compile(trg_val,re.IGNORECASE)
            # check if property value matches regex pattern
            if type(trg_val) == re.Pattern:
                return re.match(trg_val,prop_val) != None
        if prop in ["AND","OR"]:
            return element_match(el,trg_val,prop)
        if prop.lower() == "name":
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
        print(f"No matching property found (looking for property: {prop})")
        print(prop_list)
        return True
    # handle case that property list is a simple string
    if type(prop_list) == str:
        prop_list = [("name",prop_list)]
    # handle case that property list is of the form [conjunction,list]
    if prop_list[0] in ["AND","OR","and","or","And","Or"]:
        return element_match(el,prop_list[1],prop_list[0])
    # handle the case that property list is a list of (property, value) tuples
    if conjunction == "AND":
        return all([eval_cond(prop,val) for prop,val in prop_list])
    if conjunction == "OR":
        return any([eval_cond(prop,val) for prop,val in prop_list])

def select_element(el):
    # attempts to select input element
    if el:
        try:
            el.selectionitem_pattern.select()
        except Exception as error:
            print(f"Unable to select UI element with SelectionItemPattern")
            print(error)
            try:
                el.legacyiaccessible_pattern.select(0)
                print(f"Selected with legacy")
            except Exception as error:
                print(f"Unable to select UI element with LegacyIAccessiblePattern")        
                print(error)

def el_prop_val(el: ax.Element, prop_name, as_text = False):
    """Returns the property value or None if the property value cannot be retrieved"""
    try:
        if prop_name.lower() == "name":
            return el.name
        elif prop_name.lower() == "class_name":
            return el.class_name
        elif prop_name.lower() == "help_text":
            return el.help_text
        elif prop_name.lower() == "clickable_.":
            if as_text:
                loc = el.clickable_point
                return f"x: {loc.x}   y: {loc.y}"
            else:
                return el.clickable_point
        elif prop_name.lower() == "pid":
            return el.pid
        elif prop_name.lower() == "access_key":
            return el.access_key
        elif prop_name.lower() == "has_keyboard_focus":
            return el.has_keyboard_focus
        elif prop_name.lower() == "is_keyboard_focusable":
            return el.is_keyboard_focusable
        elif prop_name == "is_enabled":
            return el.is_enabled
        elif prop_name.lower() == "automation_id":
            return el.automation_id
        elif prop_name.lower() == "children":
            if as_text:
                return str(len(el.children))
            else:
                return el.children
        elif prop_name.lower() == "is_control_element":
            return el.is_control_element
        elif prop_name.lower() == "is_content_element":
            return el.is_content_element
        elif prop_name.lower() == "item_type":
            return el.item_type
        elif prop_name.lower() == "item_status":
            return el.item_status
        elif prop_name.lower() == "patterns":
            return el.patterns
        elif prop_name.lower() == "described_by":
            return el.is_described_by
        elif prop_name.lower() == "flows_to":
            return el.flows_to
        elif prop_name.lower() == "provider_description":
            return el.provider_description
        elif prop_name.lower() == "customnavigation_pattern":
            return el.customnavigation_pattern
        elif prop_name.lower() == "window_pattern":
            return el.window_pattern
        elif prop_name.lower() == "itemcontainer_pattern":
            return el.itemcontainer_pattern
        elif prop_name.lower() == "selection_pattern":
            return el.selection_pattern
        elif prop_name.lower() == "selection_pattern2":
            return el.selection_pattern2
        elif prop_name.lower() == "toggle_pattern":
            return el.toggle_pattern
        elif prop_name.lower() == "rect":
            return el.rect
        elif prop_name.lower() == "rect.x":
            return el.rect.x
        elif prop_name.lower() == "rect.y":
            return el.rect.y
        elif prop_name.lower() == "rect.width":
            return el.rect.width
        elif prop_name.lower() == "rect.height":
            return el.rect.height

    except:
        if as_text:
            return ''
        else:
            return  None

def element_information(el: ax.Element, headers = False, verbose = False):
    msg = ""
    prop_list = ["name","class_name",
                    "help_text","clickable_point",
                    "rect.x","rect.y",
                    "rect.width","rect.height","patterns"
                ]
    other_prop = [
                "pid","access_key","has_keyboard_focus",
                "is_keyboard_focusable","is_enabled","automation_id",
                "children","is_control_element","is_content_element",
                "item_type","item_status","described_by",
                "flows_to","provider_description"
            ]
    if verbose:
        prop_list += other_prop
    # Construct headers
    if headers:
        return "\t".join(prop_list)
    else:
        # Get property values
        return  "\t".join([str(el_prop_val(el,prop,as_text = True)) for prop in prop_list])

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

    def matching_elements(prop_list: list):
        """Returns a list of all UI elements that match the property list"""
        r = []
        # get list of elements
        root = ui.active_window().element
        elements = list(get_every_child(root))
        # search for match
        for el in elements:
            if element_match(el,prop_list):
                r.append(el)
        print(f"{len(r)} matching elements found")
        return r  

    def highlight_elements(elements: list):
        """Adds all ui elements in the list to the list of elements to be highlighted"""
        for el in elements:
            try:
                rect = el.rect
                el_highlights.add_element(rect)
            except:
                pass

    def clear_highlights():
        """Removes all ui elements from the highlight list"""
        el_highlights.clear_elements()
        
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

    def click_element(el: ax.Element, down_key: str='', ms: float = None):
        """clicks on the given element, with the given optional key pressed"""
        print("Attempting to run function click_element")
        if down_key != "":
            actions.key(f"{down_key}:down")

        try:
            loc = el.clickable_point
            mouse_obj = mouse_mover(loc, ms = ms, callback = ctrl.mouse_click)
        except:
            # if element doesn't have a clickable point, 
            # see if it has a rectangle
            try:
                rect = el.rect
                x = rect.x + int(rect.width/2)
                y = rect.y + int(rect.height/2)
                loc = Point2d(x,y)
                mouse_obj = mouse_mover(loc, ms = ms, callback = ctrl.mouse_click)
            except Exception as error:
                print("Sorry element is not clickable!")
                print(error)
                pass
        if down_key != "":
            actions.key(f"{down_key}:up")


    def click_focused(down_key: str=""):
        """ clicks on the currently focused element with the down key pressed"""
        actions.user.click_element(ui.focused_element(),down_key)
#        if down_key != "":
#            actions.key(f"{down_key}:down")
#        el = ui.focused_element()
#        try:
#            loc = el.clickable_point
#            mouse_obj = mouse_mover(loc,callback = ctrl.mouse_click)
#        except:
#            pass
#        if down_key != "":
#            actions.key(f"{down_key}:up")


    def mark_focused_element():
        """records the clickable point of the currently focused item"""
        global marked_elements
        el = ui.focused_element()
        print(f"Marking for selection: {element_information(el)}")
        marked_elements.append(el)
        
    def select_marked():
        """clicks on recorded marks and then empties list"""
        global marked_elements
        # clear any selection
        el = ui.focused_element()
        try:
            print(f"Removing from selection: {element_information(el)}")
            pattern = el.selectionitem_pattern
            pattern.remove_from_selection()
        except Exception as error:
            print(f"Error removing from selection in select_marked: {error}")        
        # select all marked elements
        for el in marked_elements:
            try:
                print(f"Adding to selection: {element_information(el)}")
                pattern = el.selectionitem_pattern
                pattern.add_to_selection()
            except Exception as error:
                print(f"Error adding to selection in select_marked: {error}")        
        # reset list of marked elements
        marked_elements = []


    def click_element_by_name(name: str, exact_match: bool = False):
        """Moves mouse to and clicks on element"""
        if not exact_match:
            name = f"{name}.*"
        prop_list = [("name",name)]
        elements = actions.user.matching_elements(prop_list)
        if len(elements) > 0:
            actions.user.click_element(elements[0])
    

    def highlight_elements_by_name(name: str):
        """Highlights all the elements matching the given name"""
        elements = actions.user.matching_elements(name)
        actions.user.highlight_elements(elements)
    
    def highlight_focused():
        """Highlights the focused element"""
        el = ui.focused_element()
        try:
            rect = el.rect
            print(rect)
            el_highlights.add_element(rect)
        except:
            print('no rectangle found')
        
       
       
    def select_element_by_name(name: str):
        """Selects the first UI with a matching element name. Input is interpreted as a regex pattern string"""
        # get list of elements
        elements = actions.user.matching_elements(name)
        if len(elements)  >= 1:
            select_element(elements[0])
            
    def select_matching_element(prop_list: list):
        """Attempts to select the first UI element that matches the property list"""
        # get list of elements
        elements = actions.user.matching_elements(prop_list)
        if len(elements)  >= 1:
            select_element(elements[0])

    def invoke_matching_element(prop_list: list):
        """Attempts to invoke the UI element that matches the property list"""
        # get list of elements
        elements = actions.user.matching_elements(prop_list)
        if len(elements) == 1:
            el = elements[0]
            el.invoke_pattern.invoke()
                
    def toggle_matching_element(prop_list: list):
        """Attempts to invoke the UI element that matches the property list"""
        elements = actions.user.matching_elements(prop_list)
        if len(elements) == 1:
            el = elements[0]
            el.invoke_pattern.invoke()
        

    def click_matching_element(prop_list: list, ms: int = None):
        """clicks on the element that matches property dictionary"""
        # get list of elements
        elements = actions.user.matching_elements(prop_list)
        if len(elements)  >= 1:
            el = elements[0]
            try:
                loc = el.clickable_point
                mouse_obj = mouse_mover(loc, ms = ms, callback = ctrl.mouse_click)
            except:
                # if element doesn't have a clickable point, 
                # see if it has a rectangle
                try:
                    rect = el.rect
                    x = rect.x + int(rect.width/2)
                    y = rect.y + int(rect.height/2)
                    loc = Point2d(x,y)
                    mouse_obj = mouse_mover(loc, ms = ms, callback = ctrl.mouse_click)
                except:
                    pass

    def key_to_matching_element(key: str, prop_list: list, limit: int=99, escape_key: str=None, delay: float = 0.03):
        """press given key until the first matching element is reached"""
        i = 1
        last_el = element_information(ui.focused_element(),verbose = True)
        el = ui.focused_element()
        msg = f"name: {el.name} \tclass_name: {el.class_name} \thelp_text: {el.help_text}"
        while (not element_match(ui.focused_element(),prop_list)) and (i < limit):            
            actions.key(key)
            if delay > 0:
                actions.sleep(delay)
            if (last_el == element_information(ui.focused_element(),verbose = True)) and (escape_key != None):
                actions.key(escape_key)
            i += 1

    def key_to_elem_by_val(key: str, val: str, prop: str="name", limit: int=99, escape_key: str=None, delay: float = 0.03):
        """press key until element with exact value for one property is reached"""
        prop_list = [(prop,val)]
        actions.user.key_to_matching_element(key,prop_list,limit,escape_key,delay)

    def key_to(key: str, name: str, class_name: str="",limit: int=99, escape_key: str=None, delay: float = 0.025):
        """short function name to handle common case of using a key to navigate to an element by its name and optional classname"""
        prop_list = [("name",name),("class_name",class_name)]
        actions.user.key_to_matching_element(key,prop_list,limit,escape_key,delay)


    def tab_to(name: str, class_name: str="",limit: int=99, escape_key: str=None, delay: float = 0.025):
        """short function name to handle most common case of using tab key to navigate to an element by its name and optional classname"""
        prop_list = [("name",name),("class_name",class_name)]
        actions.user.key_to_matching_element("tab",prop_list,limit,escape_key,delay)
        

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
        


    def copy_elements_accessible_by_key(key: str, limit: int=95):
        """Gets information on elements accessible by pressing the input key"""        
        elements = [element_information(ui.focused_element(),headers = True)]
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
        msg = element_information(el, headers = True)
        msg += element_information(el, verbose = True)
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

    def copy_selected_elements_to_clipboard():
        """Copies selected element information to the clipboard"""
        root = ui.active_window().element
        elements = list(get_every_child(root))
        msg = "SELECTED ELEMENT(S)\n"
        for el in elements:
            try:
                pattern = el.selectionitem_pattern                
                if pattern.is_selected:
                    msg += element_information(element) +"\n"
            except:
                pass
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
        elements = [root] + list(get_every_child(root))
        msg = element_information(root,headers = True)
        for el in elements:
            msg += "\n" + element_information(el)
        clip.set_text(msg)
        
        
        
        
        
        
        
        
        
        
        