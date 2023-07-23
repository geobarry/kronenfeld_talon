app.name: RStudio
-
tag(): user.python
show all:
	key("alt-ctrl-shift-0")
focus source:
	key('ctrl-1')
zoom source:
	key("alt-ctrl-shift-0")
	key('ctrl-shift-1')
focus console:
	key('ctrl-2')
zoom console:
	key("alt-ctrl-shift-0")
	key('ctrl-shift-2')
run all:
	key("alt-ctrl-r")
set equal:
	insert(" <- ")
check equal:
	insert(" = ")
go to line:
	key("alt-shift-g")
clear console:
	key("ctrl-l")
toggle comment:
	key('ctrl-shift-c')
replace all:
	key('ctrl-shift-J')