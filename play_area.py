from talon import app, Context,Module,actions
mod = Module()

app.notify(body="Hello world")
app.notify(title="Hello world",
           subtitle="Welcome to Talon",
           body="Enjoy your stay.",
           sound=True)

@mod.action_class
class Actions:
    def examine_selected_text_type():
        """tests the type of variable captured by the edit selected text action"""
        actions.key("f2")
        actions.sleep(0.2)
        filename = actions.edit.selected_text()
        print("TESTING DATA TYPE OF ACTIONS.EDIT.SELECTED_TEXT()")
        print(f"Value: {filename}")
        print(f"Type: {type(filename)}")
        filename = filename.replace(" ","_")
        new_file = filename[:]
        print(f"Type: {type(new_file)}")



ctx = Context()