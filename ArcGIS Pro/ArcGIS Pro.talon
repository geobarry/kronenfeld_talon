os: windows
and app.exe: arcgispro.exe

-
# MAIN MENU
menu {user.arc_menu_tab}: user.arc_open_menu_tab(arc_menu_tab)

# eventually replace these with one general command
layout {user.arc_layout_menu_item}: user.arc_invoke_menu_item("esri_layouts_homeTab",arc_layout_menu_item)
insert {user.arc_insert_menu_item}: user.arc_invoke_menu_item("esri_core_insertTab",arc_insert_menu_item)
map {user.arc_map_menu_item}: user.arc_invoke_menu_item("esri_mapping_homeTab",arc_map_menu_item)
scale bar {user.arc_scale_bar_menu_item}: user.arc_invoke_menu_item("esri_layouts_FormatTab",arc_scale_bar_menu_item)

# exceptions - menu items that require special handling
insert text: user.arc_insert_text()

# GENERAL CONVENIENCE
# say this after selecting any command that requires you to then draw a rectangle onto the layout
place (on|onto) layout: user.arc_draw_rectangle_on_layout()

# TABS (MAPS,LAYOUTS,TABLES)
# A tab is within a group, i.e. [maps,layouts,tables] or [catalog, ...]
tab close: key(ctrl-f4)
tab next: key(ctrl-f6)
tab previous: key(ctrl-shift-f6)
representative fraction: user.arc_scale_text()

# PANELS
show panels: key(ctrl:down tab)
choose panel: key(ctrl:up)
(panel|pane|tab) {user.arc_panel}:
	key(alt-v c t ctrl:down tab)
	user.key_to_elem_by_val("down","{arc_panel}.*")
	key(ctrl:up)
catalog {user.arc_catalog_group}: user.arc_select_catalog_group(arc_catalog_group)
{user.arc_button} button: user.arc_tab_to_button(arc_button)

# CONTENTS PANEL
focus contents: 
	key(alt-v c t)
	user.arc_tab_to_layers()
focus layer <user.text>:
	key(alt-v c t)
	user.arc_tab_to_layers()
	user.arc_tab_to_layer(text)
layer {user.arc_layer_context_item}: user.arc_layer_context_item(arc_layer_context_item)
list by {user.arc_contents_list_style}: user.arc_contents_list_by(arc_contents_list_style)

# SYMBOLOGY PANEL
symbology menu: key(alt j a d s)
primary symbology: user.arc_tab_to_primary_symbology()
symbol:
	user.arc_tab_to_primary_symbology()
	key(tab)
split down:
	user.key_to_elem_by_val("tab","Grid splitter")
	key(down)
split up:
	user.key_to_elem_by_val("tab","Grid splitter")
	key(up)
button burger: user.key_to_name_and_class("tab","$","Button_Burger")
properties tab:
	user.arc_symbology_tabs()
	key(right)
gallery tab:
	user.arc_symbology_tabs()
	key(left)

add data:
	key(esc:5)
	key(alt)
	sleep(0.05)
	key(m a d)
	sleep(0.25)
	key(down enter)

# ESRI shortcuts
toggle ribbon: key(ctrl-f1)
keyboard shortcuts: key(f12)
copy path: key(ctrl-alt-p)
new map: key(ctrl-m)
export: key(ctrl-e)
command search: key(alt-q)
panel options: key(alt-minus)
close panel: key(shift-esc)
next command: key(tab)
previous command: key(shift-esc)
next (element|item): key(down)
previous (element|item): key(up)
next (map|layout|view): key(ctrl-f6)
previous (map|layout|view): key(ctrl-shift-f6)

# Catalog Pane
focus catalog: key(esc:5 alt-v c p alt-f6)
focus [catalog] folders: key(esc:5 alt-v c p alt-f6 pageup f)
focus [catalogue] maps: key(esc:5 alt-v c p alt-f6 pageup m down up)
focus [catalogue] (database|databases): key(esc:5 alt-v c p alt-f6 pageup d)
focus [catalogue] layouts: key(esc:5 alt-v c p alt-f6 pageup l)
focus [catalogue] notebooks: key(esc:5 alt-v c p alt-f6 pageup n)
add folder connection: key(ctrl-shift-c)
add [geo] database connection: key(ctrl-shift-e)
project context menu: key(ctrl-shift-n)
# When folder is selected in catalog pane
new folder: key(ctrl-shift-f)
new [geo] database: key(ctrl-shift-d)
refresh: key(f5)


# Contents Pane
next layer: user.arc_contents_nav_to_layer_item("down")
previous layer: user.arc_contents_nav_to_layer_item("up")
expand: key(right)
collapse: key(left)
expand level: key(ctrl-plus)
collapse level: key(ctrl-minus)
expand all: key(ctrl-shift-plus)
collapse all: key(ctrl-shift-minus)
toggle visibility: key(space)
definition query: user.slow_key_press("enter pageup:3 down:7 tab")
export features: key(alt t v e f)
export table: key(alt t v e t)
layer properties: 
	key(menu)
	user.key_to_elem_by_val("up","Properties")
	key(enter)


# Table View
[open] attribute table: key(ctrl-t)
toggle (select|selection): key(ctrl-space)
select next: key(ctrl-enter)
select previous: key(shift-enter)
(switch|invert) selection: key(ctrl-u)
clear table selection: key(ctrl-shift-a)
next column: key(tab)
previous column: key(shift-tab)
next row: key(enter)
go first (column|cell): key(home)
go last (column|cell): key(end)
go first row: key(ctrl-up)
go last row: key(ctrl-down)
go to row: key(ctrl-g)
[custom] sort: key(ctrl-shift-s)
toggle aliases: key(ctrl-shift-n)
copy table:
	# copies contents of table for pasting into Microsoft excel
	key(ctrl-shift-a ctrl-u ctrl-shift-c)
	

# Catalogue Pane
add to current map: key(menu a)

# Map Navigation
pan west: user.pan_arcgis_pro_map('west',1)
pan east: user.pan_arcgis_pro_map("east",1)
pan north: user.pan_arcgis_pro_map('north',1)
pan south: user.pan_arcgis_pro_map('south',1)
pan tiny west: user.pan_arcgis_pro_map('west',0.2)
pan tiny east: user.pan_arcgis_pro_map('east',0.2)
pan tiny north: user.pan_arcgis_pro_map('north',0.2)
pan tiny south: user.pan_arcgis_pro_map('south',0.2)
pan west <number>: user.pan_arcgis_pro_map('west',number)
pan east <number>: user.pan_arcgis_pro_map("east",number)
pan north <number>: user.pan_arcgis_pro_map('north',number)
pan south <number>: user.pan_arcgis_pro_map('south',number)
orient [north]: key(o)
look up: 
	key(b:down)
	sleep(0.2)
	key(up:down)
	sleep(0.1)
	key(b:up)
	key(up:up)
look down: 
	key(b:down)
	sleep(0.2)
	key(down:down)
	sleep(0.1)
	key(b:up)
	key(down:up)
look right: 
	key(b:down)
	sleep(0.2)
	key(right:down)
	sleep(0.1)
	key(b:up)
	key(right:up)
look left: 
	key(b:down)
	sleep(0.2)
	key(left:down)
	sleep(0.1)
	key(b:up)
	key(left:up)





# map menu shortcuts
zoom [to] (world|full extent): key(alt-m f e)
zoom in: key(alt m z i)
zoom out: key(alt m z o)
[go to] previous extent: key(alt m p e)
[go to] next extent: key(alt m n e)

focus map:
	key(esc:5)
	key(alt)
	sleep(0.05)
	key(m)
	sleep(0.05)
	key(esc:2)
select by attributes:
	key(esc:5)
	key(alt)
	sleep(0.2)
	key(m s b a)
clear selection: key(esc:5 alt m c x)

# insert menu shortcuts
# new map command already mapped above
new layout: key(alt n n l)
new custom layout: key(alt n n l c tab:4)
(new|add) map frame: key(alt n m g)

horizontal position: user.arc_horizontal_position()

# analysis menu shortcuts
new jupyter notebook: user.slow_key_press("alt-a p f down right:3 enter",1.0)

# edit short cuts
save edits:
	key(esc:5)
	key(alt)
	sleep(0.2)
	key(e s v)
	
# layout menu shortcuts

activate map:
	key(esc:5)
	key(alt)
	sleep(0.2)
	key(y a)
close activation: user.arc_close_activation()

place straight text: 
	# make sure focuses on map layout
	key(esc:5)
	key(alt)
	sleep(0.05)
	key(m)
	sleep(0.05)
	key(esc:2)
	# navigate menu to place a straight text
	key(alt n i g)
	user.key_to_elem_by_val("tab","Straight Text")
place arrow:
	key(esc:5 alt m esc:2 alt n i g)
	user.key_to_elem_by_val("tab","Arrow")	
font size: key(alt j f f s)
# table menu shortcuts
add field:
	key(esc:5)
	key(alt)
	sleep(0.2)
	key(t v f n)
zoom [to] selected: key(alt t v r z)
flash (selected|active): key(alt t v r f)
pan [to] (selected|active): key(alt t v r p)

	
# field many shortcuts
save fields:
	key(esc:5)
	key(alt)
	sleep(0.2)
	key(f s v)
# share menu shortcuts
export layout:
	key(esc:5)
	key(alt)
	sleep(0.2)
	key(s x l)
	sleep(0.5)
	key(down:3)
# map frame menu shortcuts
[set] (text|map|legend|scale bar|north arrow|arrow|line|shape) position: 
	key(esc:5 alt j f s p)
	user.key_to_elem_by_val("tab","TextBox","class_name")
	key(ctrl-a)
flip vertical: key(alt j f r v)
flip horizontal: key(alt j f r v)
# Definition Query (and probably any other selection interface)
add [or] clause: user.arc_add_new_clause("Or")
add and clause: user.arc_add_new_clause("And")
add clause <user.word>:
	user.arc_add_new_clause("Or")
	insert(word)
	key(tab:2)