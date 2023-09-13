os: windows
and app.name: GNU Image Manipulation Program
os: windows
and app.exe: gimp-2.10.exe
-
# menus
menu file:
	key(alt-f)
menu edit:
	key(alt-e)
menu select:
	key(alt-s)
menu view:
	key(alt-v)
menu image:
	key(alt-i)
menu layer:
	key(alt-l)
menu colors:
	key(alt-c)
menu tools:
	key(alt-t)
menu filters:
	key(alt-r)
menu windows:
	key(alt-w)
menu help:
	key(alt-h)
	
#view menu
zoom in:
	key(+)
zoom out:
	key(-)
zoom <number>:
	key(alt-v)
	key(z)
	key(r)
	sleep(0.05)
	key(tab:2)
	insert(number)
	key(alt-o)