from talon import Module, ui, Context, clip, ctrl, cron
from talon.windows import ax as ax
from talon.types import Point2d as Point2d
import inspect
import math
import re


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

def get_every_child(element: ax.Element):
    if element:
        for child in element.children:
            #if child.is_keyboard_focusable:
            yield child
            yield from get_every_child(child)

ctx = Context()

mod.list("dynamic_children", desc="List of children of the active window")

@ctx.dynamic_list("user.dynamic_children")
def dynamic_children(_) -> dict[str,str]:
    root = ui.active_window().element
    elements = list(get_every_child(root))
    out = {}
    for el in elements:
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
    def focus_element_by_name(name: str):
        """Focuses on an element by name"""
        root = ui.active_window().element
        elements = list(get_every_child(root))
        for element in elements:
            if element.name == name or \
            str(element.name).lower() == name:
                element.invoke_pattern.invoke()
                break
        else:
            print("Element not found")

    def click_element_by_name(name: str):
        """Moves mouse to and clicks on element"""
        root = ui.active_window().element
        elements = list(get_every_child(root))
        for element in elements:
            if element.name == name or \
            str(element.name).lower() == name.lower():
                loc = element.clickable_point
                mouse_obj = mouse_mover(loc,ctrl.mouse_click)
                break
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
        
        msg = 'element information'
        msg += f"\nname: {el.name}"
        msg += f"\npid: {el.pid}"
        msg += f"\naccess_key: {el.access_key}"
        msg += f"\nhas_keyboard_focus: {el.has_keyboard_focus}"
        msg += f"\nis_keyboard_focusable: {el.is_keyboard_focusable}"
        msg += f"\nis_enabled: {el.is_enabled}"
        msg += f"\nautomation_id: {el.automation_id}"
        msg += f"\nclass_name: {el.class_name}"
        msg += f"\nhelp_text: {el.help_text}"
        clip.set_text(msg)
        
        
        
        
        
        
        
        
        
        
        