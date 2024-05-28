from talon import Context,Module,actions,clip,ui,ctrl

mod = Module()

mod.list("arc_panel","panels that can be accessed with standard keyboard shortcut")
mod.list("arc_button","buttons that can be accessed with standard keyboard shortcuts in ArcGIS Pro")
mod.list("arc_catalog_group","groups of items in the catalog pane")
mod.list("arc_layer_context_item","menu items available when right clicking on map layer")
mod.list("arc_menu_tab","Main menu tab automation ids")
mod.list("arc_layout_menu_item","Items on main layout menu tab")

def ensure_focus():
    """ watch out for the windows airspace popup that steals the focus!!"""
    root = ui.active_window().element
    if root.automation_id == "AirspacePopup":
        actions.user.switcher_focus("ArcGIS Pro")
        root = ui.active_window().element     

@mod.action_class
class Actions:
    def arc_navigate_to_panel(panel_name: str):
        """navigates to a currently open panel"""
        ensure_focus()
        user.key("alt-v c t ctrl:down tab")
        actions.user.key_to_elem_by_val("down","{arc_panel}.*",limit = 20,verbose = True)
        user.key("ctrl:up")
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
    def arc_add_new_clause(and_or: str="AND"):
        """adds a new clause to a definition query"""
        actions.user.key_to_matching_element("tab",[("name","Add New Clause")])
        actions.key("enter shift-tab:3")
        actions.insert(and_or)
        actions.key("tab")
    def arc_symbology_tabs():
        """From within the symbology panel, tabs to either the gallery or properties tab"""
        prop_list = ["OR",[
                        ["AND",[("name","Properties"),("class_name","ListBoxItem")]],
                        ["AND",[("name","Gallery"),("class_name","ListBoxItem")]]
                    ]]
        actions.user.key_to_matching_element("tab",prop_list,delay = 0.05)
    def arc_select_catalog_group(group_name: str):
        """Selects a group heading within the catalog panel"""
        prop_list = [("name","Catalog"),("class_name","ToolWindow")]
        el = actions.user.matching_elements(prop_list)[0]
        actions.user.invoke_element(el)
        prop_list = [("name",f"{group_name}.*"),("class_name","TextBlock.*")]
        el = actions.user.matching_elements(prop_list)[0]
        actions.user.click_element(el)
    def arc_tab_to_button(button_name: str):
        """Presses tab to reach button and then presses enter"""
        actions.user.key_to_matching_element("tab",[("name",f"{button_name}.*")],verbose = True)
    def arc_layer_context_item(item_str: str):
        """Navigates to item and presses enter"""
        print(f"item string: {item_str}")
        # make sure that we have a feature layer
        prop_list = [("automation_id","mappingTOCItem_.*Layer.*")]
        if actions.user.element_match(ui.focused_element(),prop_list):
            actions.key("menu")
            item_list = item_str.split(" ")
            for i in range(len(item_list)):
                name = item_list[i].replace("_"," ")
                prop_list = [("name",f"{name}$")]
                actions.user.key_to_matching_element("up",prop_list,limit = 25)
                if i < len(item_list) - 1:
                    actions.key("right")
        else:
            print("function arc_layer_context_item: focused element is not a feature layer")
    def arc_contents_nav_to_layer_item(up_or_down: str = "down",layer_type: str = ""):
        """navigates the contents panel to the next/previous layer item"""
        # Error Checking
        if up_or_down.lower() not in ["up","down"]:
            return 
        if layer_type not in ["FeatureLayer","RasterLayer","VectorTileLayer","TiledServiceLayer"]:
            layer_type = ""
        # first navigate to a table of contents item
        prop_list = [("automation_id",".*TOCItem.*")]
        actions.user.key_to_matching_element("tab",prop_list)
        # press key at least once
        actions.key(up_or_down)
        # navigate to next layer item
        if layer_type == "":
            prop_list = ["OR",[
                ("automation_id","mappingTOCItem_FeatureLayer.*"),
                ("automation_id","mappingTOCItem_RasterLayer.*"),
                ("automation_id","mappingTOCItem_VectorTileLayer.*"),
                ("automation_id","mappingTOCItem_TiledServiceLayer.*"),
            ]]
        else:
            prop_list = [("automation_id",f"mappingTOCItem_{layer_type}.*")]
        actions.user.key_to_matching_element(up_or_down,prop_list)
    def arc_open_menu_tab(automation_id: str):
        """Opens the menu; use talon list user.arc_menu_tab"""
        # get parent element
        ensure_focus()
        root = ui.active_window().element
        # dig down one element at a time for speed
        prop_list = [("automation_id","RibbonControl")]
        RibbonControl = actions.user.matching_element(prop_list,root = root,max_level = 1)
        # Every other menu tab except Project is under the tab strip
        prop_list = [("automation_id","PART_TabStrip")]
        TabStrip = actions.user.matching_element(prop_list,root = RibbonControl,max_level = 1)
        prop_list = [("automation_id",automation_id)]
        el = actions.user.matching_element(prop_list,root = TabStrip,max_level = 1)
        if el == None:
            # Project menu tab is directly underneath the ribbon control
            el = actions.user.matching_element(prop_list,root = RibbonControl,max_level = 1)
        el.invoke_pattern.invoke()
    def arc_draw_rectangle_on_layout():
        """Draws rectangle in center of layout, to be repositioned later"""
        prop_list = [("class_name","LayoutPaneView")]
        el = actions.user.matching_element(prop_list,max_level = 10)
        x = el.rect.x + int(el.rect.width/3)
        y = el.rect.y + int(el.rect.height/3)
        ctrl.mouse_move(x,y)
        actions.user.mouse_drag(0)
        x = el.rect.x + int(2*el.rect.width/3)
        y = el.rect.y + int(2*el.rect.height/3)        
        ctrl.mouse_move(x,y)        
        actions.user.mouse_drag_end()
    def arc_horizontal_position():
        """Sets focus on horizontal position"""
        actions.user.arc_open_menu_tab("esri_layouts_FormatTab")
        prop_list = [("automation_id","X")]
        actions.user.key_to_matching_element("tab",prop_list,limit = 45)
    def arc_scale_text():
        """Places focus on the scale text element"""
        prop_list = [("value","1:.*")]
        el = actions.user.matching_element(prop_list)
        actions.user.click_element(el)
    def arc_close_activation():
        """Closes the active map on the current layout"""
        actions.user.arc_open_menu_tab("esri_layouts_ActivateMapTab")
        prop_list = [("automation_id","esri_layouts_deactivateMap")]
        actions.user.key_to_matching_element("tab",prop_list)
        actions.key("enter")
    def arc_invoke_menu_item(menu_id: str,item_id: str):
        """Invokes item on layout menu"""
        actions.user.arc_open_menu_tab(menu_id)
        actions.sleep(0.1)
        prop_list = [("automation_id",item_id)]
        actions.user.key_to_matching_element("tab",prop_list)
        el = ui.focused_element()
#        el = actions.user.matching_element(prop_list,max_level = 6)
        el.invoke_pattern.invoke()
ctx = Context()

