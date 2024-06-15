from talon import Module, ui, Context, clip, ctrl, cron, actions
from talon.windows import ax as ax
from talon.types import Point2d as Point2d

mod = Module()
ctx = Context()

def set_position(left=None,top=None,width=None,height=None):
    """Gets the left, top, width and height of focused element"""
    # right click to open the format panel
    actions.key("menu o right")

    # tab to gallery button
    prop_list = [("class_name","NetUIGalleryButton")]
    actions.user.key_to_matching_element("tab",prop_list,delay = 0.05,verbose = False)

    # press right to get to the Size & Properties gallery button
    prop_list = [("name","Size & Properties")]
    actions.user.key_to_matching_element("right",prop_list,delay = 0.05,verbose = False)

    # press tab to get to the Size group
    prop_list = [("name","Size"),("class_name","NetUIRibbonButton")]        
    actions.user.key_to_matching_element("tab",prop_list,verbose = False,delay = 0.07)

    # makes sure the toggle is open
    actions.user.toggle_for_next_value("Height","enter",verbose=False)

    # get width and height
    actions.key("tab")
    if height != None:
        ui.focused_element().value_pattern.value = str(height)
        actions.key("enter")
    actions.key("tab")
    if width != None:
        ui.focused_element().value_pattern.value = str(width)
        actions.key("enter")

    # press tab to get to the Position group
    prop_list = [("name","Position"),("class_name","NetUIRibbonButton")]        
    actions.user.key_to_matching_element("tab",prop_list,verbose = False,delay = 0.07)

    # makes sure the toggle is open
    actions.user.toggle_for_next_value("Horizontal position","enter",verbose=False)

    # get horizontal position (left)
    actions.key("o ctrl-a")
    if left != None:
        ui.focused_element().value_pattern.value = str(left)
        actions.key("enter")
    actions.key("tab:2 ctrl-a")
    if top != None:
        ui.focused_element().value_pattern.value = str(top)
        actions.key("enter")
    
    # exit panel
    actions.user.slow_key_press("ctrl-space c")
def get_position():
    """Gets the left, top, width and height of focused element"""
    # right click to open the format panel
    actions.key("menu o right")

    # tab to gallery button
    prop_list = [("class_name","NetUIGalleryButton")]
    actions.user.key_to_matching_element("tab",prop_list,delay = 0.05,verbose = False)

    # press right to get to the Size & Properties gallery button
    prop_list = [("name","Size & Properties")]
    actions.user.key_to_matching_element("right",prop_list,delay = 0.05,verbose = False)

    # press tab to get to the Size group
    prop_list = [("name","Size"),("class_name","NetUIRibbonButton")]        
    actions.user.key_to_matching_element("tab",prop_list,verbose = False,delay = 0.07)

    # makes sure the toggle is open
    actions.user.toggle_for_next_value("Height","enter",verbose=False)

    # get width and height
    actions.key("tab")
    height = actions.user.el_prop_val(ui.focused_element(),"value")
    height = float(height.replace('"',''))
    actions.key("tab")
    width = actions.user.el_prop_val(ui.focused_element(),"value")
    width = float(width.replace('"',''))

    # press tab to get to the Position group
    prop_list = [("name","Position"),("class_name","NetUIRibbonButton")]        
    actions.user.key_to_matching_element("tab",prop_list,verbose = False,delay = 0.07)

    # makes sure the toggle is open
    actions.user.toggle_for_next_value("Horizontal position","enter",verbose=False)

    # get horizontal position (left)
    actions.key("o ctrl-a")
    left = actions.user.el_prop_val(ui.focused_element(),"value")
    left = float(left.replace('"',''))
    actions.key("tab:2 ctrl-a")
    top = actions.user.el_prop_val(ui.focused_element(),"value")
    top = float(top.replace('"',''))
    
    # exit panel
    actions.user.slow_key_press("ctrl-space c")
    
    return left,top,width,height

@mod.action_class
class Actions:
    def power_exit_ribbon():
        """Exits the ribbon while retaining the selected element"""
        # Works on the observation that ribbon selection elements
        # have class names that start with "NetUI"
        i = 0
        while actions.user.element_match(ui.focused_element(),[("class_name","NetUI.*")]) and i < 7:
            actions.key("esc")
            i += 1
    def power_position(horizontal_or_vertical: str = "",val: float = None):
        """navigates to the position section of the powerpoint format panel"""
        # right click to open the format panel
        actions.key("menu o right")
        # tab to gallery button
        prop_list = [("class_name","NetUIGalleryButton")]
        actions.user.key_to_matching_element("tab",prop_list,delay = 0.05,verbose = False)
        # press right to get to the Size & Properties gallery button
        prop_list = [("name","Size & Properties")]
        actions.user.key_to_matching_element("right",prop_list,delay = 0.05,verbose = False)
        # press tab to get to the Horizontal Position group
        prop_list = [("name","Position"),("class_name","NetUIRibbonButton")]        
        actions.user.key_to_matching_element("tab",prop_list,verbose = False)
        # makes sure the toggle is open
        actions.user.toggle_for_next_value("Horizontal position","enter",verbose=False)
        # set value if specified
        if horizontal_or_vertical.lower() in ["horizontal","vertical"]:
            if horizontal_or_vertical.lower() == "horizontal":
                actions.key("o")
            else:
                actions.key("v")
            if val != None:
                actions.sleep(0.1)
                actions.insert(val)
                actions.key("enter ctrl-space c")
    def power_tab_format_panel_top_row():
        """Presses tab until one of the icons on the top of the format panel is reached"""
        icon_names = ["Effects","Fill & Line","Picture", "Size & Properties"]
        i = 1
        limit = 15
        actions.sleep(0.2)
        val = actions.user.el_prop_val("name")
        while (not val in icon_names) and (i < limit):
            print(f"FUNCTION: power_tab_format_panel_top_row: {val}")
            actions.key("tab")
            actions.sleep(0.02)
            val = actions.user.el_prop_val("name")
            i += 1
        actions.sleep(0.05)
    def power_crop_picture(pos: str):
        """Initiates a crop action"""
        actions.key("alt j p v c")
        actions.sleep(0.5)
        def do_crop(bearing,x_offset,y_offset):
            actions.user.move_mouse_to_focused_element(pos,x_offset,y_offset)
            actions.user.eagle_set_bearing(bearing)
        if pos == "upper left":
            do_crop(135,5,5)
        elif pos == "lower left":
            do_crop(45,5,-5)
        elif pos == "upper right":
            do_crop(225,-5,5)
        elif pos == "lower right":
            do_crop(315,-5,-5)
        elif pos == "left":
            do_crop(90,5,0)
        elif pos == "right":
            do_crop(270,-5,0)
        elif pos == "top":
            do_crop(180,0,5)
        elif pos == "bottom":
            do_crop(0,0,-5)
    def power_notes_adjust_height(dh: int, direction: int = 1):
        """direction: 1 = up   -1 = down"""
        gap = 18 # mouse has to be placed as many pixels above top of notes panel
        dh = dh * direction
        prop_list = [("name","Slide Notes")]
        el = actions.user.matching_element(prop_list)
        # If notes are hidden, coordinates will be ridiculously negative
        if el.rect.x < -1000000:
            actions.user.power_toggle_notes()
            actions.sleep(0.3)
            el = actions.user.matching_element(prop_list)
            try:
                cur_ht = el.rect.height
                dh -= cur_ht
            except:
                pass
        x = el.rect.x + int(el.rect.width/2)
        y = el.rect.y - gap        
        ctrl.mouse_move(x,y)
        actions.user.mouse_drag(0)
        actions.user.slow_mouse(x,y - dh,callback = actions.user.mouse_drag_end)
    def power_toggle_notes():
        """Hides or restores notes pane"""
        prop_list = [("name","Notes"),("class_name","NetUISimpleButton")]
        el = actions.user.matching_element(prop_list)
        el.invoke_pattern.invoke()
    def power_go_to_slide(n: int):
        """Quickly navigate to a slide by number"""
        keys = ["f5"] + [x for x in str(n)] + ["enter","esc"]
        for key in keys:
            actions.key(key)
    def power_paste_adjacent(hnd_pos: str):
        """Pastes what's on the clipboard to the indicated position relative to the currently selected element; use user.handle_position"""
        # get position of currently selected element
        anchor_left,anchor_top,anchor_width,anchor_height = get_position() 
        actions.key("ctrl-v")
        # get position of newly pasted element
        left,top,width,height = get_position()

        # calculate position of element to paste
        if "top" in hnd_pos or "upper" in hnd_pos:
            top = anchor_top - height
        elif "bottom" in hnd_pos or "lower" in hnd_pos:
            top = anchor_top + anchor_height
        else:
            top = anchor_top
        if "left" in hnd_pos:
            left = anchor_left - width
        elif "right" in hnd_pos:
            left = anchor_left + anchor_width
            print(f'anchor_left: {anchor_left}')
            print(f'anchor_width: {anchor_width}')
            print(f'left: {left}')
        else:
            left = anchor_left
        set_position(top = top,left = left)