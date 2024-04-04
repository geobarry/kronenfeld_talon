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
        actions.user.move_mouse_to_focused_element(pos)
        if pos == "upper left":
            actions.user.eagle_set_bearing(135)
        elif pos == "lower left":
            actions.user.eagle_set_bearing(45)
        elif pos == "upper right":
            actions.user.eagle_set_bearing(225)
        elif pos == "lower right":
            actions.user.eagle_set_bearing(315)
        elif pos == "left":
            actions.user.eagle_set_bearing(90)
        elif pos == "right":
            actions.user.eagle_set_bearing(270)
        elif pos == "top":
            actions.user.eagle_set_bearing(180)
        elif pos == "bottom":
            actions.user.eagle_set_bearing(0)
            
    def power_go_to_slide(n: int):
        """Quickly navigate to a slide by number"""
        keys = ["f5"] + [x for x in str(n)] + ["enter","esc"]
        for key in keys:
            actions.key(key)

            