os: windows
and app.exe: arcgispro.exe

-
# A tab is within a group, i.e. [maps,layouts,tables] or [catalog, ...]
tab close: key(ctrl-f4)
tab next: key(ctrl-f6)
tab previous: key(ctrl-shift-f6)
show panels: key(ctrl:down tab)
choose panel: key(ctrl:up)
focus contents: key(alt-v c t)

do test:
	print("Is this working?")

list by drawing order:
    user.mouse_helper_position_save()
    user.mouse_helper_move_image_relative("ArcGIS Pro list by drawing order.png", 0)
    sleep(0.05)
    mouse_click(0)
    sleep(0.05)
    user.mouse_helper_position_restore()

list by data source:
    user.mouse_helper_position_save()
    user.mouse_helper_move_image_relative("ArcGIS Pro list by data source.png", 0)
    sleep(0.05)
    mouse_click(0)
    sleep(0.05)
    user.mouse_helper_position_restore()

symbology menu: key(alt j a d s)
symbology (pain|pane|panel): key(alt j a d s esc enter)

focus Geoprocessing:
	key(alt-v c t)
	sleep(0.25)
	key(alt-v t s)
	sleep(0.25)
    user.mouse_helper_move_image_relative("ArcGIS Pro Geoprocessing selected.png", 0, 20, 50)
	mouse_click(0)

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
expand: key(right)
collapse: key(left)
expand level: key(ctrl-plus)
collapse level: key(ctrl-minus)
expand all: key(ctrl-shift-plus)
collapse all: key(ctrl-shift-minus)
toggle layer: key(space)
layer properties: key(menu p)
definition query: user.slow_key_press("menu p pageup:3 down:7 tab")
toggle (label|labels|labeling): key(menu b)
(label|labels|labeling) properties: key(menu o)
remove layer: user.slow_key_press("menu r")
export features: key(alt t v e f)
export table: key(alt t v e t)

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

# Catalogue Pane
add to current map: key(menu a)

# Map Navigation
pan west: user.pan_arcgis_pro_map('west',1)
pan east: user.pan_arcgis_pro_map("east",1)
pan north: user.pan_arcgis_pro_map('north',1)
pan south: user.pan_arcgis_pro_map('south',1)
pan tiny west: user.pan_arcgis_pro_map('west',0.1)
pan tiny east: user.pan_arcgis_pro_map('east',0.1)
pan tiny north: user.pan_arcgis_pro_map('north',0.1)
pan tiny south: user.pan_arcgis_pro_map('south',0.1)
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



# MAIN MENU
menu project:
	key(esc:5)
	key(alt)
	sleep(0.2)
	key(p)
menu map:
	key(esc:5)
	key(alt)
	sleep(0.2)
	key(m)
menu insert:
	key(esc:5)
	key(alt)
	sleep(0.2)
	key(n)
menu analysis:
	key(esc:5)
	key(alt)	
	sleep(.2)
	key(a)
menu view: 
	key(esc:5)
	key(alt)
	sleep(0.2)
	key(v)
menu edit:
	key(esc:5)
	key(alt-	
	sleep(0.2)
	key(e)
menu imagery:
	key(esc:5)
	key(alt)
	sleep(0.2)
	key(i)
menu share:
	key(esc:5)
	key(alt)
	sleep(0.2)
	key(s)
menu layout:
	key(esc:5)
	key(alt)
	sleep(0.2)
	key(y)
menu table:
	key(esc:5)
	key(alt)
	sleep(0.2)
	key(t)
	key(v)
menu lay out:
	key(esc:5)
	key(alt)
	sleep(0.2)
	key(j l)
menu animation:
	key(esc:5)
	key(alt)
	sleep(0.2)
	key(x a)
menu map frame: key(esc:5 alt j 5) 

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
insert map: key(alt n m g)

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
close activation: key(esc:5 alt j l c)
	
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
[set] map position: key(esc:5 alt j f s p)
