hello hello:
	speech.disable()
hello come in:
	speech.disable()
hello come on in:
	speech.disable()
hello what's up:
	speech.disable()
open up <user.text>:
	insert(text)
	sleep(0.05)
	key(enter)
(my|bee jay) name:
	insert("Barry Kronenfeld")
(my|bee jay) gmail:
	insert("barrykronenfeld@gmail.com")
(my|bee jay) (email|mail):
	insert("bjkronenfeld@eiu.edu")

dotcom:
	insert(".com")
daddy to you:
	insert(".edu")

(numb|number) phrase <user.formatters> <user.text> <number>:
	insert(user.formatted_text(text, formatters))
	insert(" ")
	insert(number)

(numb|number) phrase <user.text> <number>:
	insert(text)
	insert(" ")
	insert(number)
(numb|number) phrase <number> <user.text>:
	insert(number)
	insert(" ")
	insert(text)
(numb|number) phrase <number> <user.text> <number>:
	insert(number_1)
	insert(" ")
	insert(text)
	insert(" ")
	insert(number_2)
(numb|number) phrase <user.text> <number> <user.text>:
	insert(text_1)
	insert(" ")
	insert(number)
	insert(" ")
	insert(text_2)
(numb|number) phrase <number> <user.text> <number> <user.text>:
	insert(number_1)
	insert(" ")
	insert(text_1)
	insert(" ")
	insert(number_2)
	insert(" ")
	insert(text_2)
(numb|number) phrase <user.text> <number> <user.text> <number>:
	insert(text_1)
	insert(" ")
	insert(number_1)
	insert(" ")
	insert(text_2)
	insert(" ")
	insert(number_2)
	



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
launch:
	key(super)
	sleep(0.2)
show cheat sheet:
	key(super)
	sleep(0.2)
	insert("Anaconda")
	sleep(0.25)
	key(enter)
	sleep(2.5)
	insert("cd %appdata%/Talon/user/kronenfeld_talon/cheat sheet")
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
up jiggle:
	key(up)
	sleep(0.05)
	key(down)
switch (application|applications):
	key(alt-tab)
switch (other|second) application:
	key(alt:down)
	key(tab:3)
	key(alt:up)
switch third application:
	key(alt:down)
	key(tab:4)
	key(alt:up)
delete line:
	edit.line_start()
	edit.line_start()
	edit.line_start()
	edit.line_start()
	edit.extend_line_end()
	key(backspace:2)
stop: 
	user.mouse_scroll_stop()
	user.stop_repeating()
shutdown computer:
	key(super)
	sleep(0.2)
	key(up)
	sleep(0.1)
	key(right)
	key(enter)
	sleep(0.1)
	key(down:2)
	sleep(0.1)
	key(enter)

	
	