os: windows
and app.name: qgis-bin.exe
os: windows
and app.exe: qgis-bin.exe
-
add vector layer: key(ctrl-shift-v)
add (geodatabase|geo database): 
	key(ctrl-shift-v)
	sleep(0.1)
	key(alt-d tab:2 alt-down pageup down)
	
remove layer:
	key(menu r)
	sleep(0.5)
	key(enter)
add shape file:
	key(ctrl-shift-v tab:6)
	sleep(0.2)
	key(space)
	sleep(0.2)
	key(tab down e down:2 enter shift-tab)
	
	
