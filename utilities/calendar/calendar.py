from talon import Module, Context, actions
import os
mod = Module()

@mod.action_class
class Actions:
    def show_calendar():
        """opens the calendar web page"""
        # Calendar webpage file is same as current .py file but with HTML extension
        calendar_file = os.path.abspath(__file__)[:-3] + ".html"
        actions.user.open_url(calendar_file)
    def calendar_next_month():
        """navigates to the next month in the calendar"""
        prop_list = [("name","chevron_right")]
        el = actions.user.matching_element(prop_list,max_level = 13)
        el.invoke_pattern.invoke()
    def calendar_previous_month():
        """navigates to the previous month in the calendar"""
        prop_list = [("name","chevron_left")]
        el = actions.user.matching_element(prop_list,max_level = 13)
        el.invoke_pattern.invoke()

ctx = Context()
