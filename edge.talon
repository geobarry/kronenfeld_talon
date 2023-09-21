os: windows
and app.name: Microsoft Edge
os: windows
and app.exe: msedge.exe

-
refresh:
	key(ctrl-f5)
[toggle] full screen:
	key(f11)
[toggle] read aloud:
	key(ctrl-shift-u)
read aloud:
	key(ctrl-minus)
	sleep(0.05)
	key(left)
	key(enter)
address bar:
	key(alt-d)
move tab to window:
	key(alt-d)
	key(ctrl-a)
	key(ctrl-c)
	key(ctrl-w)
	key(ctrl-n)
	sleep(0.1)
	key(alt-d) 
	key(ctrl-a)
	key(ctrl-v)
	key(enter)
