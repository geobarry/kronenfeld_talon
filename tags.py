from talon import Module, Context, actions

mod = Module()
# this declares a tag in the user namespace (i.e. 'user.tabs')
mod.tag("python", desc="apps that use my own python commands")
mod.tag("jupyter_notebook", desc="apps that use my own jupyter notebook commands")
mod.tag("fast_spots", desc="eliminates need to say 'spot' to click on screen spots")
mod.tag("zoom", desc = "in a zoom meeting")

@mod.action_class
class Actions:
    def activate(tag_name: str):
        """Add a tag to the activated tags list"""
        cur_tags.append(f"user.{tag_name}")
        ctx.tags = cur_tags
        print(cur_tags)
    def deactivate(tag_name: str):
        """Remove a tag from the activated tags list"""
        cur_tags.remove(f"user.{tag_name}")
        ctx.tags = cur_tags
        print(cur_tags)
        
ctx = Context()
cur_tags = [tag for tag in ctx.tags]