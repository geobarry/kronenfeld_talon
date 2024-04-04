from talon import Context,Module,actions,clip

mod = Module()

@mod.action_class
class Actions:
    def pan_arcgis_pro_map(direction: str, duration: float):
        """Pans the map for duration expressed relative to the default duration 
        which is 0.5 seconds."""
        if direction == 'west':
            key = 'left'
        elif direction == 'east':
            key = 'right'
        elif direction == 'north':
            key = 'up'
        elif direction == 'south':
            key = 'down'
        else:
            return None
        actions.key("{}:down".format(key))
        print("pan_arcgis_pro_map duration: {}".format(duration))
        actions.sleep(duration * 0.5)
        actions.key("{}:up".format(key))
    def arc_tab_to_layers():
        """presses the tab key to get to the layer list area"""
        print(f"FUNCTION: arc_tab_to_layers")
        actions.user.key_to_matching_element("tab",["OR",[("class_name","TreeView"),("class_name","TreeViewItem")]],escape_key = "esc")
    def arc_tab_to_layer(layer_name: str):
        """presses the down key to get to the specified layer"""
        actions.user.key_to_matching_element("down",[("name",layer_name)])
    def arc_tab_to_primary_symbology():
        """presses the tab key to get to the primary symbology combo box"""
        actions.user.key_to_matching_element("tab",[("name","Selected primary symbology")])
    def tab_to_name(name: str):
        """Presses tab into reaching an element whose name is ok"""
        actions.user.key_to_matching_element("tab",[("name",name)])
    def arc_add_new_clause(and_or: str="AND"):
        """adds a new clause to a definition query"""
        actions.user.key_to_matching_element("tab",[("name","Add New Clause")])
        actions.key("enter shift-tab:3")
        actions.insert(and_or)
        actions.key("tab")
        
ctx = Context()