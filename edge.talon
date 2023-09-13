os: windows
and app.name: Microsoft Edge
os: windows
and app.exe: msedge.exe
-
toggle read aloud:
	key(ctrl-shift-u)
read aloud:
	key(ctrl-minus)
	sleep(0.05)
	key(left)
	key(enter)