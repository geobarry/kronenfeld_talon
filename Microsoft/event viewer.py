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
    def ev_next_bug_check(limit: int = 9):
        """Moves down the list to the next bug check"""
        # determine where in the list we are already
        start = 0
        el = ui.focused_element()
        i = el.automation_id[13:]
        print(f"automation_id: {el.automation_id}")
        print(f'current element id: {i}')
        if i.isnumeric():
            print(f"starting at item {i}")
            start = int(i)
        else:
            print("could not find current element id")
        prop_list = [("automation_id","mainListView")]
        el = actions.user.matching_element(prop_list,max_level = 13)
        print(f"number of the events: {len(el.children)}")
        print(f"#3 element: {el.children[3].name}")
        for el in el.children[start + 3:]:
            if el.children[2].name == "BugCheck":
                el.invoke_pattern.invoke()
                break
ctx = Context()