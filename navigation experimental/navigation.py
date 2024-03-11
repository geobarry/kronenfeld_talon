import itertools
import re

from talon import Context, Module, actions, settings

ctx = Context()
mod = Module()

mod.setting(
    "text_nav_max_char_search",
    type=int,
    default=300,  
    desc="The maximum number of characters that will be included in the search for the keywords above and below in <user direction>",
)


@mod.action_class
class Actions:
    def slide_selection_to_match(match_text: str):
        """shifts selection to the left or to the right up to the length of 
        match_text to match the given text"""
        # get current selection
        sel = actions.edit.selected_text()
        
        # initialize match positions to a number that is definitely too high
        left_match_pos, right_match_pos = len(match_text),len(match_text)
        
        # see how far we would have to slide left by cutting off the beginning of match_text
        # > the end of match_text will match the start of the current selection
        
        for i in range(len(match_text)):
            if match_text[i:] in sel:
                left_match_pos = i
                break
        # try sliding right
        for i in range(len(match_text)):
            if match_text[:-i] in sel:
                right_match_pos = i
                break
                
        # take the smaller number
        if left_match_pos < right_match_pos:
            match_pos = -left_match_pos
            arrow = 'left'
        else:
            match_pos = right_match_pos
            arrow = 'right'
            
        # perform slide only match position is smaller than initialized value
        if abs(match_pos) < len(match_text):
            actions.user.slide_selection(arrow,match_pos)
        
        
    def slide_selection(arrow: str, num_char: int = 1):
        """test function to figure out how to adjust the selection one character"""
        print(arrow)
        if arrow == "right":
            forward = "right"
            backward = "left"
            extend_forward = actions.edit.extend_right
        else:
            forward = "left"
            backward = "right"
            extend_forward = actions.edit.extend_left
            
        sel = actions.edit.selected_text()
        actions.user.move_cursor(backward)
        for i in range(num_char):
            actions.user.move_cursor(forward)
        actions.sleep(0.05)
        for i in range(len(sel)):
            extend_forward()
            
    def test_find(search_string: str):
        """test to see what talons find function does"""
        msg = actions.edit.find(search_string)
        # answer: uses the applications built-in find function
    def adjust_selection(search_string: str, max_adj: int=3):
        """called this after searching for a string to adjust selection
        in cases where search results in an off by one or two error"""
        sel = actions.edit.selected_text()
        for i in range(max_adj):
            if sel.find(search_string[i:]) == 0:
                pass
                
    def dynamic_text_search(search_string: str, occurrence_number: int=1):
        """Test how fast we can move selection one character at a time"""
        # Answer: too slow for searching but fast enough for post search revision
        i = 0
        match = False
        while i < settings.get("user.text_nav_max_char_search") and not match:
            i += 1
            actions.edit.extend_left()
            sel = actions.edit.selected_text()
            if sel[:len(search_string)] == search_string:
                match = True
        

def match_backwards(regex, occurrence_number, subtext):
    try:
        match = list(regex.finditer(subtext))[-occurrence_number]
        return match
    except IndexError:
        return


def match_forward(regex, occurrence_number, sub_text):
    try:
        match = next(
            itertools.islice(regex.finditer(sub_text), occurrence_number - 1, None)
        )
        return match
    except StopIteration:
        return None
