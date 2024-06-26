from talon import Module, ui, Context, clip, ctrl, cron, actions, canvas, screen
from talon.windows import ax as ax
from talon.types import Point2d as Point2d
from talon.skia import  Paint
import inspect
import math
import re
from io import StringIO

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
    def remove_element(self,rect):
        self.rectangles.remove(rect)
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
        if len(self.rectangles) > 0:
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
            print("have to calculate milliseconds")
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
        if self.completed >= self.num_intervals:
            print(f"moving mouse to x: {self.dest.x}")
            ctrl.mouse_move(self.dest.x,self.dest.y)
            cron.cancel(self.job)
            if self.callback != None:
                print("calling callback function")
                self.callback()
        else:
            # handle previous moves
            self.completed += 1
            x = round(self.orig[0] + self.interval_x * self.completed)
            y = round(self.orig[1] + self.interval_y * self.completed)
            ctrl.mouse_move(x,y)

mod = Module()

mod.list("handle_position","position for grabbing ui elements")    
mod.list("nav_key","keys commonly used to navigate UI elements")

def match(el: ax.Element, prop_list: list, conjunction: str="AND", verbose: bool = False):
    """Returns true if the element matches all of the properties in the property dictionary"""
    # prop_list is either a list of form [(property, trg_val),...]
    #     where trg_val is either a string (for case-insensitive match at start of string)
    #     or a regex expression
    # or a list of ["OR",list] or ["AND",list]
    # or just a string, in which case property will be "name"
    # Conditions in the top level list are connected with an AND conjunction
    def eval_cond(prop,trg_val):
        if verbose:
            print(f'prop: {prop}')
            print(f'trg_val: {trg_val}')
        def value_match(prop_val,trg_val):
            # if trg_val is a string, convert to a regex pa'ttern
            if verbose:
                print("inside value_match sub function")
            if type(trg_val) != re.Pattern:
#            if type(trg_val) == str:
                trg_val = str(trg_val)
                trg_val = re.compile(trg_val,re.IGNORECASE)
            if verbose:
                print(f'trg_val: {trg_val}')
                print(f'type(trg_val): {type(trg_val)}')
                print("Let's try converting this to a string")
                print(str(trg_val))
            # check if property value matches regex pattern...
            
            if type(trg_val) == re.Pattern:
                if verbose:
                    print(f'trg_val: {trg_val}')
                    print(f'prop_val: {prop_val}')
                    print(f"regex match: {re.match(trg_val,prop_val)}")
                return re.match(trg_val,prop_val) != None
        if prop in ["AND","OR"]:
            return match(el,trg_val,prop)
        elif prop == "clickable":
            clickable = True
            try:
                loc = el.clickable_point
            except:
                clickable = False
            finally:
                return trg_val == clickable
        else:
            prop_val = actions.user.el_prop_val(el, prop, as_text = True)
            if verbose:
                print(f'prop_val: {prop_val}')
                print(f"type: {type(prop_val)}")
                print(f"value_match: {value_match(prop_val, trg_val)}")
            return value_match(prop_val, trg_val)
        # if something is not properly specified, return true so that other conditions can be evaluated
        print("ERROR in function actions.user.element_match (accessibility.py)")
        print(f"No matching property found (looking for property: {prop})")
        print(prop_list)
        return True
    # handle case that property list is a simple string
    if type(prop_list) == str:
        prop_list = [("name",prop_list)]
    # handle case that property list is of the form [conjunction,list]
    if prop_list[0] in ["AND","OR","and","or","And","Or"]:
        r = match(el,prop_list[1],prop_list[0])
    # handle the case that property list is a list of (property, value) tuples
    elif conjunction == "AND":
        r =  all([eval_cond(prop,val) for prop,val in prop_list])
    elif conjunction == "OR":
        r = any([eval_cond(prop,val) for prop,val in prop_list])
    # next line as for debugging
    if verbose:
        print(f"{r} | element: {el.name[:25]} | rule: {prop_list}")
    return r
def get_element_tree(el: ax.Element, max_level: int = 7):
    # do a breadth first search keeping track of levels, ids and parents
    print("Getting element tree ...")
    cur_level = 0
    el_id = -1
    parent_id = -1
    Q = []
    r = []
    Q.append((cur_level,parent_id,el))    
    while len(Q) > 0:        
        cur_level,parent_id,el = Q.pop(0)
        if cur_level <= max_level:
            el_id += 1
            r.append((cur_level,el_id,parent_id,el))
            for child in el.children:
                Q.append((cur_level+1,el_id,child))
        
    return r
def get_every_child(el: ax.Element, cur_level: int = 0, max_level: int = 7):
    # possibly keeping elements in memory is very expensive,
    # might be better to find some way to do what you want with element properties
    if cur_level <= max_level:
        if el:
            yield el
            for child in el.children:
                yield from get_every_child(child,cur_level + 1,max_level)

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
    def slow_mouse(x: int, y: int, ms: int = None, callback: any = None):
        """moves the mouse slowly towards the target"""
        loc = Point2d(x,y)
        mouse_obj = mouse_mover(loc, ms = ms,callback = callback)
    def el_prop_val(el: ax.Element, prop_name: str, as_text: bool = False):
        """Returns the property value or None if the property value cannot be retrieved"""
        try:
            if prop_name.lower() == "name":
                return el.name
            elif prop_name.lower() == "class_name":
                return el.class_name
            elif prop_name.lower() == "automation_id":
                return el.automation_id
            elif prop_name.lower() == "printout":
                s = StringIO()
                print(el,file = s)
                # remove new line at end, as well as <> that break copy/paste into Excel
                x = s.getvalue().strip().replace("<","").replace(">","") 
                return x                
            elif prop_name.lower() == "help_text":
                return el.help_text
            elif prop_name.lower() == "culture":
                return el.culture
            elif prop_name.lower() == "is_control_element":
                return el.is_control_element
            elif prop_name.lower() == "is_content_element":
                return el.is_content_element
            elif prop_name.lower() == "is_password":
                return el.is_password
            elif prop_name.lower() == "window_handle":
                return el.window_handle
            elif prop_name.lower() == "item_type":
                return el.item_type
            elif prop_name.lower() == "is_offscreen":
                return el.is_offscreen
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
            elif prop_name.lower() == "children":
                if as_text:
                    return str(len(el.children))
                else:
                    return el.children
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
            elif prop_name.lower() == "children":
                return el.children
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
            elif prop_name.lower() == "value":
                return el.value_pattern.value
            elif prop_name.lower() == "value.is_read_only":
                return el.value_pattern.is_read_only
            elif prop_name.lower() == "legacy.value":
                return el.legacyiaccessible_pattern.value
            elif prop_name.lower() == "legacy.selection":
                return el.legacyiaccessible_pattern.selection
        except:
            if as_text:
                return ''
            else:
                return  None
    def element_location(el: ax.Element):
        """Returns a point that can be clicked on, or else None"""
        try: # try clickable point property
            print("accessibility: element_location: trying clickable point")
            return el.clickable_point
        except:
            try: # try rectangle
                print("accessibility: element_location: trying rectangle center")
                rect = el.rect
                print(f'rect: {rect}')
                return Point2d(rect.x + int(rect.width/2),rect.y + int(rect.height/2))
            except:
                print("accessibility: element_location: NO LOCATION FOUND :(")
                return None
    def element_match(el: ax.Element, prop_list: list, conjunction: str="AND", verbose: bool = False):
        """Returns true if the element matches all of the properties in the property dictionary"""
        return match(el,prop_list,conjunction,verbose)
    def element_exists(prop_list: list):
        """Returns true if an element where the given properties exists"""
        root = ui.active_window().element
        elements = list(get_every_child(root))
        for el in elements:
            if actions.user.element_match(el,prop_list):            
                return True
        return False
    def element_list():
        """returns_a_list_of_all_elements"""
        root = ui.active_window().element
        return list(get_every_child(root))
    def matching_element(prop_list: list, item_num: int = 0, max_level: int = 12,root: ax.Element = None):
        """returns the zero based nth item matching the property list, or None"""
        if root == None:
            root = ui.active_window().element
        matches = actions.user.matching_elements(prop_list,max_level = max_level,root = root)
        if len(matches) > item_num:
            return matches[item_num]
        else:
            return None
    def matching_elements(prop_list: list, max_level: int = 12, root: ax.Element = None):
        """Returns a list of all UI elements under the root that match the property list"""
        print(f'root: {root}')
        print(f'prop_list: {prop_list}')
        print(f'max_level: {max_level}')
        r = []
        # get list of elements
        if root == None:
            root = ui.active_window().element
        elements = list(get_every_child(root,max_level = max_level))
        # search for match
        for el in elements:
            try:
                if actions.user.element_match(el,prop_list):
                    r.append(el)
            except:
                pass
        print(f"function matching_elements: {len(r)} matching elements found")
        return r  
    def select_element(el: ax.Element):
        """ attempts to select input element"""
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
    def hover_element(el: ax.Element, ms: float = None):
        """hovers on the given element"""
        loc = actions.user.element_location(el)
        if loc != None:    
            mouse_obj = mouse_mover(loc, ms = ms)
    def click_element(el: ax.Element, down_key: str='', ms: float = None):
        """clicks on the given element, with the given optional key pressed"""
        print("Attempting to run function click_element")
        loc = actions.user.element_location(el)
        if loc != None:
            if down_key != "":
                actions.key(f"{down_key}:down")
            def do_callback():
                ctrl.mouse_click()
                if down_key != "":
                    actions.key(f"{down_key}:up")                
            mouse_obj = mouse_mover(loc, ms = ms, callback = do_callback)
    def invoke_element(el: ax.Element):
        """attempts to invoke element"""
        try:
            pattern = el.invoke_pattern
            pattern.invoke()
        except Exception as error:
            print(f"Error in invoke_element: {error}")
    def highlight_elements(elements: list):
        """Adds all ui elements in the list to the list of elements to be highlighted"""
        for el in elements:
            try:
                rect = el.rect
                el_highlights.add_element(rect)
            except:
                print('Unable to highlight element: no rectangle found')
    def highlight_element(el: ax.Element):
        """Highlights a single element"""
        actions.user.highlight_elements([el])
    def remove_highlight(el: ax.Element):
        """Remove element from highlights"""
        try:
            el_highlights.remove_element(el.rect)
        except:
            print("Unable to remove highlight: Element rectangle does not match any current highlight")
    def clear_highlights():
        """Removes all ui elements from the highlight list"""
        el_highlights.clear_elements()
    def highlight_focused():
        """Highlights the focused element"""
        actions.user.highlight_elements([ui.focused_element()])
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
        try:
            val = actions.user.element_property_value(property_name)
        except:
            pass
        actions.key(rev_key)
        return val
    def toggle_for_next_value(trg: str, toggle_key: str, advance_key: str="tab", property_name: str="name", verbose: bool = False):
        """Toggles current element until the next elements value meets the target value"""
        cur_val = actions.user.peek_next_property_value(property_name,advance_key)
        if verbose:
            print(f"cur_val: {cur_val}")
        if cur_val != trg:
            actions.key(toggle_key)
    def hover_focused():
        """Hovers the mouse on the currently focused element"""
        actions.user.hover_element(ui.focused_element())
    def click_focused(down_key: str=""):
        """clicks on the currently focused element with the down key pressed"""
        actions.user.click_element(ui.focused_element(),down_key)
    def mark_focused_element():
        """records the clickable point of the currently focused item"""
        global marked_elements
        el = ui.focused_element()
        marked_elements.append(el)
    def select_marked():
        """selects marked elements and then empties list"""
        global marked_elements
        # clear any selection
        el = ui.focused_element()
        try:
            pattern = el.selectionitem_pattern
            pattern.remove_from_selection()
        except Exception as error:
            print(f"Error removing from selection in accessibility.py function select_marked: {error}")        
        # select all marked elements
        for el in marked_elements:
            try:
                pattern = el.selectionitem_pattern
                pattern.add_to_selection()
            except Exception as error:
                print(f"Error adding to selection in accessibility.py function select_marked: {error}")        
        # reset list of marked elements
        marked_elements = []
    def select_matching_element(prop_list: list):
        """Attempts to select the first UI element that matches the property list"""
        # get list of elements
        elements = actions.user.matching_elements(prop_list)
        if len(elements)  >= 1:
            actions.user.select_element(elements[0])
    def invoke_matching_element(prop_list: list, item_num: int = 0, max_level: int = 99):
        """Attempts to invoke the UI element that matches the property list"""
        el = actions.user.matching_element(prop_list,item_num = item_num,max_level = max_level)
        if el != None:
            actions.user.invoke_element(el)
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
    def key_to_matching_element(key: str, prop_list: list, limit: int=39, escape_key: str=None, delay: float = 0.03, verbose: bool = False):
        """press given key until the first matching element is reached"""
        i = 1        
        # if the previous action has not completed an error can occur
        # (e.g. PowerPoint accessing format panel from context menu)
        # to avoid this, wrap in try except clause 
        def focused_element():
            n = 0
            while n < 3:
                try:
                    return ui.focused_element()
                except:
                    n += 1
                    actions.sleep(delay)
            return None
        el = focused_element()
        last_el = el
        msg = f"name: {el.name} \tclass_name: {el.class_name} \thelp_text: {el.help_text}"
        if verbose:
            print(f"ELEMENT: {el.name}")
        if el:
            try:
                while (not actions.user.element_match(el,prop_list,verbose = verbose)) and (i < limit):            
                    actions.key(key)
                    if delay > 0:
                        actions.sleep(delay)
                    el = ui.focused_element()
                    if el:
                        if verbose:
                            print(f"ELEMENT: {el.name}")      
                        if (last_el == ui.focused_element()) and (escape_key != None):
                            actions.key(escape_key)
                        last_el = el
                        i += 1
                    else:
                        break
            except Exception as error:
                print(error)
            if actions.user.element_match(el,prop_list):
                return el
            else:
                return None
    def key_to_elem_by_val(key: str, val: str, prop: str="name", limit: int=99, escape_key: str=None, delay: float = 0.03):
        """press key until element with exact value for one property is reached"""
        prop_list = [(prop,val)]
        actions.user.key_to_matching_element(key,prop_list,limit,escape_key,delay)
    def key_to_name_and_class(key: str, name: str, class_name: str = ".*",limit: int=99,delay: float = 0.03):
        """Press key until element with matching name and classes reached"""
        prop_list = [("name",name),("class_name",class_name)]
        actions.user.key_to_matching_element(key,prop_list,limit = limit,delay = delay)
    def invoke_by_value(val: str, prop: str = "name", max_level: int = 99):
        """Searches for first element with given property value and invokes it."""
        prop_list = [prop,val]
        el = actions.user.matching_element(prop_list,max_level = max_level)
        actions.user.invoke_element(el)
    def hover_element_by_name(name: str, exact_match: bool = False):
        """Moves mouse to element"""
        if not exact_match:
            name = f"{name}.*"
        prop_list = [("name",name)]
        elements = actions.user.matching_elements(prop_list)
        if len(elements) > 0:
            actions.user.hover_element(elements[0])
    def click_element_by_name(name: str, exact_match: bool = False):
        """Moves mouse to and clicks on element"""
        if not exact_match:
            name = f"{name}.*"
        prop_list = [("name",name)]
        elements = actions.user.matching_elements(prop_list)
        if len(elements) > 0:
            actions.user.click_element(elements[0])
    def select_element_by_name(name: str, exact_match: bool = False):
        """Selects the first UI with a matching element name."""
        if not exact_match:
            name = f"{name}.*"
        elements = actions.user.matching_elements([("name",name)])
        if len(elements)  >= 1:
            actions.user.select_element(elements[0])
    def highlight_elements_by_name(name: str, exact_match: bool = False):
        """Highlights all the elements matching the given name"""
        if not exact_match:
            name = f"{name}.*"
        elements = actions.user.matching_elements(name)
        actions.user.highlight_elements(elements)
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
    def element_information(el: ax.Element, headers: str = False, verbose: str = False):
        """Returns information separated by tabs that can be pasted into a spreadsheet"""
        msg = ""
        prop_list = ["name","class_name",
                        "help_text","automation_id",
                        "printout","value",
                        "children","patterns",
                        "is_offscreen",
                        "clickable_point",
                        "rect.x","rect.y",
                        "rect.width","rect.height"
                    ]
        other_prop = [
                    "pid","access_key","has_keyboard_focus",
                    "is_keyboard_focusable","is_enabled",
                    "children","is_control_element","is_content_element",
                    "item_type","item_status","described_by",
                    "flows_to","provider_description",
                    "value.is_read_only",
                    "legacy.value","legacy.selection"
                ]
        if verbose:
            prop_list += other_prop
        # Construct headers
        if headers:
            return "\t".join(prop_list)
        else:
            # Get property values
            return  "\t".join([str(actions.user.el_prop_val(el,prop,as_text = True)) for prop in prop_list])
    def copy_elements_accessible_by_key(key: str, limit: int=50, delay: int = 0.03, verbose: bool = True):
        """Gets information on elements accessible by pressing the input key"""        
        i = 1
        el = ui.focused_element()
        msg = actions.user.element_information(el, verbose = verbose)
        if verbose:
            full_msg = msg
        else:
            full_msg = actions.user.element_information(el,verbose = True)
        messages = [actions.user.element_information(el,verbose = verbose,headers = True)]
        full_msgs = []
        while (not full_msg in full_msgs) and (i < limit):
            messages.append(msg)
            full_msgs.append(full_msg)
            actions.sleep(delay)
            actions.key(key)
            try:
                el = ui.focused_element()
            except:
                print("Could not obtain next element, try increasing delay.")
            el = ui.focused_element()
            msg = actions.user.element_information(el, verbose = verbose)    
            if verbose:
                full_msg = msg
            else:
                full_msg = actions.user.element_information(el,verbose = True)
            i += 1
        clip.set_text("\n".join(messages))
    def copy_mouse_elements_to_clipboard():
        """Copies elements with rectangle containing current mouse position"""
        pos = ctrl.mouse_pos()
        root = ui.active_window().element
        elements = list(get_every_child(root))
        n = 0
        msg = actions.user.element_information(elements[0],headers = True)
        for el in elements:
            r = actions.user.el_prop_val(el,"rect")
            if r:
                if (r.x < pos[0] < r.x + r.width) and (r.y < pos[1] < r.y + r.height):
                    msg += "\n" + actions.user.element_information(el)
                    n += 1                
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
        msg = actions.user.element_information(el, headers = True, verbose = True)
        msg += "\n" + actions.user.element_information(el, verbose = True)
        clip.set_text(msg)
    def copy_focused_element_with_children(levels: int = 1):
        """Copies information about currently focused element and children to the clipboard"""
        el = ui.focused_element()
        actions.user.copy_elements_to_clipboard(levels,el)
    def copy_enabled_element_to_clipboard():
        """Searches for the first enabled element and copies is information to the clipboard"""
        root = ui.active_window().element
        elements = list(get_every_child(root))
        msg = "ENABLED ELEMENT(S)\n"
        for element in elements:
            if element.is_enabled:
                msg += actions.user.element_information(element) +"\n"
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
                    msg += actions.user.element_information(element) +"\n"
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
                msg += actions.user.element_information(element) +"\n"
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
                    msg += actions.user.element_information(element) +"\n"
                except:
                    pass 
        clip.set_text(msg)
    def copy_elements_to_clipboard(max_level: int = 7, root: ax.Element = None):
        """Attempts to retrieve all properties from all elements"""
        print("INSIDE FUNCTION COPY ELEMENTS TO CLIPBOARD")
        if root == None:
            root = ui.active_window().element
        # mark elements with special status
        # focused element
        focused_el = ui.focused_element()
        prop_list = ["name","class_name","automation_id","printout"]
        focus_fingerprint = [actions.user.el_prop_val(focused_el,prop) for prop in prop_list]
        # mouse elements
        mouse_fingerprints = []
        pos = ctrl.mouse_pos()
        def el_data(level,cur_id,parent_id,el):
            status = []
            # check to see if this is the focused element
            el_fingerprint = [actions.user.el_prop_val(el,prop) for prop in prop_list]
            if el_fingerprint == focus_fingerprint:
                status.append("focused")
            # check to see if mouse is on element
            r = actions.user.el_prop_val(el,"rect")
            if r:
                if (r.x < pos[0] < r.x + r.width) and (r.y < pos[1] < r.y + r.height):
                    status.append("mouse")
            status = "|".join(status)
            r = f"{status}\t{level}\t{cur_id}\t{parent_id}\t" + re.sub(r"\r?\n","<<new line>>",actions.user.element_information(el)) 
            print(f'{r}')
            return r
        el_info = get_element_tree(root,max_level = max_level)
        print(f"{len(el_info)} elements in tree...")
        msg = "status\tlevel\tid\tparent_id\t" + actions.user.element_information(root,headers = True)
        messages = [el_data(level,cur_id,parent_id,el) for level,cur_id,parent_id,el in el_info]
        clip.set_text(msg + "\n" + "\n".join(messages))

        
        