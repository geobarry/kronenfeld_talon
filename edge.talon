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
[toggle] immersive reader:
	key(f9)
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
clear cache:
	key(ctrl-shift-del)
	sleep(2)
	key(tab:11)
	key(enter)
	sleep(0.3)
	user.tab_close_wrapper()
# for use in gmail (to delete emails)
mark for deletion:
	key(x)
	sleep(0.2)
	key(down)

