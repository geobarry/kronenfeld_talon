os: windows
and app.exe: ArcGISPro.exe
-
toggle ribbon:
	key(ctrl-f1)
tab close:
	key(ctrl-f4)
map next:
	key(ctrl-f6)
map previous:
	key(ctrl-shift-f6)
focus contents:
	key(alt-v)
	key(c)
	key(t)
	sleep(0.25)
    user.mouse_helper_move_image_relative("ArcGIS Pro contents selected.png", 0, -25, 235)
	mouse_click(0)
	key(shift-tab)

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
pan west:
	user.pan_arcgis_pro_map('west',1)
pan east:
	user.pan_arcgis_pro_map("east",1)
pan north:
	user.pan_arcgis_pro_map('north',1)
pan south:
	user.pan_arcgis_pro_map('south',1)
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
	sleep(0.05)
	key(m)
menu insert:
	key(esc:5)
	key(alt-n)
menu analysis:
	key(esc:5)
	key(alt-a)	
menu view: 
	key(esc:5)
	key(alt-v)
menu edit:
	key(esc:5)
	key(alt-e)	
menu imagery:
	key(esc:5)
	key(alt-i)	
menu share:
	key(esc:5)
	key(alt-s)
menu layout:
	key(esc:5)
	key(alt-y)
menu table:
	key(esc:5)
	key(alt)
	sleep(0.1)
	key(t)
	key(v)
show panels:
	key(ctrl:down)
	key(tab)
choose panel:
	key(ctrl:up)