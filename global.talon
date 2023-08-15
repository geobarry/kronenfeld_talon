undo:
	key(ctrl-z)
(we do)|(redo):
	key(ctrl-y)
focus taskbar:
	key(super-b)
punch <number>:
	edit.right()
	repeat(number_1 - 1)
	insert(' ')
right parent:
	insert(")")
[left] parent:
	insert("(")
inside (parent|parents):
	user.insert_between('(',')')
inside (angle|angles):
	user.insert_between('<','>')
alt:
	key('alt')
show cheat sheet:
	key(super)
	sleep(0.2)
	insert("Anaconda")
	sleep(0.25)
	key(enter)
	sleep(2.5)
	insert("cd %appdata%/Talon/user/cheat sheet")
	key("enter")
	insert("python -m http.server 8080")
	key("enter")
	key(super)
	sleep(0.2)
	insert("Edge")
	sleep(0.5)
	key("enter")
	sleep(0.3)
	insert("localhost:8080/cheatsheet.html")
	key("enter")
release keys:
	key(shift:up)
	key(ctrl:up)
	key(alt:up)
	key(super:up)
escape out:
	key(esc)
	key(esc)
	key(esc)
	key(esc)
	key(esc)
save:
	key(ctrl-s)
search:
	key(ctrl-f)
tab jiggle:
	key(tab)
	sleep(0.05)
	key(shift-tab)
F6 jiggle:
	key(f6)
	sleep(0.05)
	key(shift-f6)
right jiggle:
	key(right)
	sleep(0.05)
	key(left)
left jiggle:
	key(left)
	sleep(0.5)
	key(right)
down jiggle:
	key(down)
	sleep(0.05)
	key(up)
	