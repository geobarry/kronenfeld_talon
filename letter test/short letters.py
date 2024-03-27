from talon import Context, Module, actions


mod = Module()
mod.list("letter_short", desc="letters as you say them")

@mod.action_class
class Actions:
    def insert_joined(str_list: list):
        """Joins a list of strings into a single string and inserts"""
        actions.insert("".join(str_list))
        
ctx = Context()

