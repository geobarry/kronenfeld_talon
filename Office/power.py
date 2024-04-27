from talon import Module, ui, Context, clip, ctrl, cron, actions
from talon.windows import ax as ax
from talon.types import Point2d as Point2d

mod = Module()
ctx = Context()

@mod.action_class
class Actions:
    def power_tab_format_panel_top_row():
        """Presses tab until one of the icons on the top of the format panel is reached"""
        icon_names = ["Effects","Fill & Line","Picture", "Size & Properties"]
        i = 1
        limit = 15
        val = actions.user.element_property_value("name",sleep_time=0.2)
        while (not val in icon_names) and (i < limit):
            print(f"FUNCTION: power_tab_format_panel_top_row: {val}")
            actions.key("tab")
            val = actions.user.element_property_value("name")
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
            
    def power_go_to_slide(n: int):
        """Quickly navigate to a slide by number"""
        keys = ["f5"] + [x for x in str(n)] + ["enter","esc"]
        for key in keys:
            actions.key(key)

            