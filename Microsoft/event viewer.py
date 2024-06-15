from talon import Context,Module,actions,clip,ui
from talon.windows import ax as ax

mod = Module()

def event_info(el: ax.Element):    
    r = {
        "Level":el.children[0].name,
        "Date and Time":el.children[1].name,
        "Source":el.children[2].name,
        "Event ID":el.children[3].name,
        "Task Category":el.children[4].name
        }
    return r
    
@mod.action_class
class Actions:
    def ev_filter_current_log():
        """Invokes the filter current log button"""
        prop_list = [("name","Filter Current Log..."),("class_name","TaskButton")]
        el = actions.user.matching_element(prop_list)
        el.invoke_pattern.invoke()
    def ev_next_bug_check(limit: int = 499):
        """Moves down the list to the next bug check"""

        # determine where in the list we are already
        i = 0
        el = ui.focused_element()
        while el.children[2].name != "BugCheck" and i < limit:
            actions.key("down")
            el = ui.focused_element()
            i += 1
            actions.sleep(0.07)
ctx = Context()