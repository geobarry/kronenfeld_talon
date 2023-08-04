os: windows
and app.exe: ArcGISPro.exe
-
focus contents:
	key(alt-v)
	key(c)
	key(t)
	sleep(0.25)
    user.mouse_helper_move_image_relative("ArcGIS Pro contents selected.png", 0, -25, 235)
	mouse_click(0)

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

attribute table:
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
	key(esc)
	key(esc)
	key(esc)
	key(esc)
	key(esc)

	key(alt)
	sleep(0.05)
	key(m)
	key(a)
	key(d)
	sleep(0.25)
	key(down)
	key(enter)

zoom in:
	key(esc)
	key(esc)
	key(esc)
	key(esc)
	key(esc)

	key(alt)
	sleep(0.05)
	key(m)
	key(z)
	key(i)
zoom out:
	key(esc)
	key(esc)
	key(esc)
	key(esc)
	key(esc)

	key(alt)
	sleep(0.05)
	key(m)
	key(z)
	key(o)
	
focus map:
	key(esc)
	key(esc)
	key(esc)
	key(esc)
	key(esc)

	key(alt)
	sleep(0.05)
	key(m)
	sleep(0.05)
	key(esc)
	key(esc)

pan right:
	user.mouse_helper_move_image_relative("ArcGIS Pro map icon.png", 0, 99, 100)
	user.mouse_drag(0)
	sleep(0.05)
	user.mouse_helper_move_image_relative("ArcGIS Pro map icon.png", 0, 100, 100)
	sleep(0.1)
	user.mouse_helper_move_image_relative("ArcGIS Pro map icon.png", 0, 101, 100)
	sleep(0.1)
	user.mouse_helper_move_image_relative("ArcGIS Pro map icon.png", 0, 200, 100)
	sleep(0.1)
	user.mouse_drag_end()

map:
	key(esc)
	key(esc)
	key(esc)
	key(esc)
	key(esc)

	key(alt)
	sleep(0.05)
	key(m)

insert:
	key(esc)
	key(esc)
	key(esc)
	key(esc)
	key(esc)

	key(alt-n)
	
analysis:
	key(esc)
	key(esc)
	key(esc)
	key(esc)
	key(esc)

	key(alt-a)
	
view: 
	key(esc)
	key(esc)
	key(esc)
	key(esc)
	key(esc)

	key(alt-v)

edit:
	key(esc)
	key(esc)
	key(esc)
	key(esc)
	key(esc)

	key(alt-e)
	
imagery:
	key(esc)
	key(esc)
	key(esc)
	key(esc)
	key(esc)

	key(alt-i)
	
share:
	key(esc)
	key(esc)
	key(esc)
	key(esc)
	key(esc)

	key(alt-s)