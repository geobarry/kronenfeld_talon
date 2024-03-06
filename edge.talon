os: windows
and app.name: Microsoft Edge
os: windows
and app.exe: msedge.exe

-
# official keyboard shortcuts ()
focus favorites: key(alt-shift-b)
focus toolbar: key(alt-shift-t)
settings: key(alt-e)
open downloads: key(ctrl-j)
duplicate tab: key(ctrl-shift-k)
refresh: key(ctrl-f5)
(open|reopen) last [closed]: key(ctrl-shift-t)
toggle fit: key(ctrl-backslash)
rotate: key(ctrl-rbrack)
clear browsing data: key(ctrl-shift-del)
focus content: key(ctrl-f6)
immersive reader: key(f9)
caret browsing: key(f7)

[toggle] full screen: key(f11)
[toggle] read aloud: key(ctrl-shift-u)
[toggle] immersive reader: key(f9)
address bar: key(alt-d)
move tab to window:
	key(alt-d ctrl-a ctrl-c ctrl-w ctrl-n)
	sleep(0.1)
	key(alt-d ctrl-a ctrl-v enter)
clear cache:
	key(ctrl-shift-del)
	sleep(2)
	key(tab:11)
	key(enter)
	sleep(0.3)
	user.tab_close_wrapper()
	
# for use in devtools
show console: key(ctrl-shift-j)
show elements: key(ctrl-shift-c)
shows settings: key(f1)
next panel: key(ctrl-rbrack)
previous panel: key(ctrl-brack)
show command [menu]: key(ctrl-shift-p)

# for use in gmail (to delete emails)
mark for deletion:
	key(x)
	sleep(0.2)
	key(down)

# downloads - assumes that downloads are showing
save download [as]: user.slow_key_press("ctrl-j tab:2 enter",1.0)
show [in] folder: user.slow_key_press("menu down:2 enter")

	
	