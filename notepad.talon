app.name: Notepad++
- 
go to line: key(ctrl-g)
go to line <number>:
	key(ctrl-g)
	sleep(0.1)
	insert("{number}")
	key(enter)
open (work space|workspace): key(alt-f w enter)
toggle (work space|workspace): key(alt-shift-w)
focus (work space|workspace): key(alt-shift-w:2)
zoom in: key(alt-v down:6 right enter)
zoom out: key(alt-v down:6 right down enter)
select block: key(ctrl-alt-b)

	
# commands for talon files
press key: user.insert_between('key(',')')
sleep: user.insert_between('sleep(',')')
open containing folder: key(alt-f o shift-tab:2)

# were going to set this up for JavaScript
#variable:
#	insert("var ")
set equal:
	insert(" = ")
#define function:
#	user.insert_between("function ","(){}")
report message:
	user.insert_between('console.log("','")')
report variable:
	user.insert_between('console.log(',')')

# MENUS
file menu: key(alt-f)
edit menu: key(alt-e)
search menu: key(alt-s)
view menu: key(alt-v)
encoding menu: key(alt-n)
language menu: key(alt-l)
settings menu: key(alt-t)
tools menu: key(alt-o)
macro menu: key(alt-m)
run menu: key(alt-r)
plugins menu: key(alt-p)
window menu: key(alt-w)
question menu: key(alt-shift-/)

# FOR DEMONSTRATIONS
file menu save as: user.slow_key_press("alt-f down:7 space:5 enter",0.15)
