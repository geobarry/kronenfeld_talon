from talon import Context,Module,actions
mod = Module()

@mod.action_class
class Actions:
    def change_volume(amount: int=10):
        """Raises the master volume for up to five apps"""
        actions.key("super-ctrl-v")
        actions.sleep(0.7)
        actions.key("tab:3")
        actions.key("down:25")
        actions.key("tab:3")
        actions.key("enter")
        actions.sleep(1.0)
        actions.key("tab:8")
        actions.sleep(0.1)
        if amount > 0:
            actions.key("right:{}".format(amount))
        else:
            amount = -amount
            actions.key("left:{}".format(amount))
        actions.key("alt-f4")

ctx = Context()