from talon import Context,Module,actions,clip,ui,ctrl
from talon.windows import ax as ax
import re
mod = Module()

mod.list("spyder_panel","Panels  in the spyder application")


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
    def spyder_capture_module_names():
        """Navigates project tree to capture module names"""
        actions.user.spyder_focus_panel("Project")
        # get children of current element
        el = ui.focused_element()
        r = ''
        for child in el.children:
            if child.name[-3:] == ".py":
                r += child.name[:-3] + "\n"
        clip.set_text(r)
ctx = Context()