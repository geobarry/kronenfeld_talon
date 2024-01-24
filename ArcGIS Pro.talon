os: windows
and app.exe: ArcGISPro.exe
-
toggle ribbon:
	key(ctrl-f1)
# A tab is within a group, i.e. [maps,layouts,tables] or [catalog, ...]
tab close:
	key(ctrl-f4)
tab next:
	key(ctrl-f6)
tab previous:
	key(ctrl-shift-f6)
show panels:
	key(ctrl:down)
	key(tab)
choose panel:
	key(ctrl:up)

focus contents:
	key(alt-v c t)
#	key(c)
#	key(t)
#	sleep(0.25)
#    user.mouse_helper_move_image_relative("ArcGIS Pro contents selected.png", 0, #-25, 235)
	#mouse_click(0)
	#key(shift-tab)

expand all:
	key(ctrl+)
collapse all:
	key(ctrl-)

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

[open] attribute table:
	key(ctrl-t)
symbology menu:
	key(alt)
	key(j)
	key(a)
	key(d)
	key(s)
symbology (pain|pane|panel):
	key(alt)
	key(j)
	key(a)
	key(d)
	key(s)
	key(esc)
	key(enter)
focus catalog:
	key(alt-v)
	key(c)
	key(p)
	sleep(0.25)
    user.mouse_helper_move_image_relative("ArcGIS Pro catalog selected.png", 0, 53, 287)
	mouse_click(0)
focus Geoprocessing:
	key(alt-v)
	key(c)
	key(t)
	sleep(0.25)

	key(alt-v)
	key(t)
	key(s)
	sleep(0.25)
    user.mouse_helper_move_image_relative("ArcGIS Pro Geoprocessing selected.png", 0, 20, 50)
	mouse_click(0)

add data:
	key(esc:5)
	key(alt)
	sleep(0.05)
	key(m)
	key(a)
	key(d)
	sleep(0.25)
	key(down)
	key(enter)

pan west:
	user.pan_arcgis_pro_map('west',1)
pan east:
	user.pan_arcgis_pro_map("east",1)
pan north:
	user.pan_arcgis_pro_map('north',1)
pan south:
	user.pan_arcgis_pro_map('south',1)
pan tiny west:
	user.pan_arcgis_pro_map('west',0.1)
pan tiny east:
	user.pan_arcgis_pro_map('east',0.1)
pan tiny north:
	user.pan_arcgis_pro_map('north',0.1)
pan tiny south:
	user.pan_arcgis_pro_map('south',0.1)
pan west <number>:
	user.pan_arcgis_pro_map('west',number)
pan east <number>:
	user.pan_arcgis_pro_map("east",number)
pan north <number>:
	user.pan_arcgis_pro_map('north',number)
pan south <number>:
	user.pan_arcgis_pro_map('south',number)
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

# map menu shortcuts
zoom [to] (world|full extent):
	key(alt-m f e)
zoom in:
	key(esc:5)
	key(alt)
	sleep(0.05)
	key(m)
	key(z)
	key(i)
zoom out:
	key(esc:5)
	key(alt)
	sleep(0.05)
	key(m)
	key(z)
	key(o)	
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
clear selection:
	key(esc:5)
	key(alt)
	sleep(0.2)
	key(m c l)
	
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
	
# table menu shortcuts
add field:
	key(esc:5)
	key(alt)
	sleep(0.2)
	key(t v f n)
	
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
