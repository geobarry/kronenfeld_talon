from talon import Context,Module,actions,clip,ui
from talon.windows import ax as ax
import re
mod = Module()

mod.list("word_equation_menu_item","items that can be accessed from the equation menu")
mod.list("word_equation_script","equation superscript and subscript structures")

@mod.action_class
class Actions:
    def word_display_markup(display_option: str):
        """Selects what markup to show when tracking changes"""
        actions.key("alt r z t t d")
        actions.user.key_to_elem_by_val("down",display_option)
        actions.key("enter esc esc")
    def word_go_to_comments():
        """Navigates to the comment pane"""
        prop_dict = ["OR",[
                        ("name","New comment"),
                        ("name","Comment thread.*"),
                        ("name","Like"),
                        ("name","More thread actions"),
                        ("class_name","NetUIElement")
                    ]]
        actions.user.key_to_matching_element("f6",prop_dict,limit = 7)
    def word_go_to_main_text():
        """Navigates to the main text panel"""
        prop_dict = [("name",".*\.docx?$")]
        actions.user.key_to_matching_element("f6",prop_dict,limit = 7)
    def word_open_menu(tab_name: str):
        """Selects the menu tab with a given name"""
        actions.key("esc:5")
        prop_list = [("name",tab_name),("class_name","NetUIRibbonTab")]
        el = actions.user.matching_element(prop_list)
        actions.user.select_element(el)
        return el
    def word_open_menu_item(tab_name: str,item_info: str):
        """Expand, toggle or invoke menu item"""
        # open the menu tab
        parent = actions.user.word_open_menu(tab_name)
        # create property list for item we want to expand toggle or invoke
        item_info = item_info.split(",")
        prop_list = [("name",item_info[0]),("class_name",item_info[1]),("automation_id",item_info[2])]
        # At this point I would like to find element from accessibility tree but it seems like
        # the menu tab element does not have any children
        # so we're going to have to tab our way there
        actions.user.key_to_matching_element("tab",prop_list,delay = 0.07)
        actions.sleep(0.05)
        el = ui.focused_element()
        if "ExpandCollapse" in el.patterns:
            el.expandcollapse_pattern.expand()
        elif "Toggle" in el.patterns:
            el.toggle_pattern.toggle()
        elif "Invoke" in el.patterns:
            el.invoke_pattern.invoke()
    def word_equation_script(structure_name: str):
        """Creates a subscript, superscript, etc inside an equation"""
        actions.user.word_open_menu_item("Equation","Script,NetUIAnchor,EquationScriptGallery")
        actions.sleep(0.05)
        prop_list = [("name",structure_name)]
        actions.key("pageup home")
        actions.user.key_to_matching_element("right",prop_list,delay = 0.07)
        actions.key("enter")
ctx = Context()
#