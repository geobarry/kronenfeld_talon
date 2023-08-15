app.name: Notepad++
- 
# commands for talon files
(key|he):
	user.insert_between('key(',')')
sleep:
	user.insert_between('sleep(',')')
repeat <number>:
	insert("repeat({number})")
# were going to set this up for JavaScript
go to line:
	key(ctrl-g)
toggle workspace:
	key(alt-shift-W)
variable:
	insert("var ")
set equal:
	insert(" = ")
define function:
	user.insert_between("function ","(){}")
report message:
	user.insert_between('console.log("','")')
report variable:
	user.insert_between('console.log(',')')
zoom in:
	key(alt-v)
	key(down)
	repeat(5)
	key(right)
	key(enter)
zoom out:
	key(alt-v)
	key(down)
	repeat(5)
	key(right)
	key(down)
	key(enter)
select block:
	key(ctrl-alt-b)

	