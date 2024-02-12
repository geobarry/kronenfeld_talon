os: windows
-
# disabling talon
hello hello: speech.disable()
[hello] come [on] in$: speech.disable()
hello what's up: speech.disable()
computer [go to] sleep: speech.disable()
computer stop listening: speech.disable()
computer close your ears: speech.disable()

	
# windows volume
volume up: key(volup)
volume down: key(voldown)
volume mute: key(mute)

# windows keyboard shortcuts
launch explorer: key(super-e)
screen snip: key(super-shift-s)
toggle Bluetooth: 
	key(super-a)
	sleep(1)
	key(right)
	sleep(0.5)
	key(tab enter)
	sleep(0.7)
	key(space esc)	
		
# cross application common shortcuts
save: key(ctrl-s)	
search: key(ctrl-f)
context menu: key(menu)
	
# websites and system paths
open up <user.text>:
	insert(text)
	sleep(0.05)
	key(enter)
open up <user.letter>:
	key(letter)
	sleep(0.05)
	key(enter)
open up <number>:
	insert("{number}")
	sleep(0.15)
	key(enter)
# common words
(my|bee jay) name:
	insert("Barry Kronenfeld")
my first name:
	insert("Barry")
	
(my|bee jay) gmail:
	insert("barrykronenfeld@gmail.com")
(my|bee jay) (email|mail):
	insert("bjkronenfeld@eiu.edu")
dotcom:
	insert(".com")
daddy to you:
	insert(".edu")

inside inches:
	user.insert_between('"', '"')
inside feet:
	user.insert_between("'", "'")

(numb|number) phrase <user.formatters> <user.text> <number>:
	insert(user.formatted_text(text, formatters))
	insert(" ")
	insert(number)

(numb|number) phrase <user.text> <number>:
	insert(text)
	insert(" ")
	insert("{number}")
(numb|number) phrase <number> <user.text>:
	insert("{number}")
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
	insert("{number}")
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
	
enter object:
	key(f2)


undo:
	key(ctrl-z)
redo$:
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
(inside (parent|parents)|parentheses):
	user.insert_between('(',')')
inside (angle|angles):
	user.insert_between('<','>')
alt:
	key('alt')
launch:
	key(super)
	sleep(1.0)
update cheat sheet:
	user.cheatsheet()
	sleep(1.5)
	key(super)
	sleep(0.2)
	insert("Anaconda")
	sleep(0.25)
	key(enter)
	sleep(2.5)
	insert("cd %appdata%/Talon/user/kronenfeld_talon/cheat sheet")
	key(enter)	
	insert("pandoc -s cheatsheet.md -c cheatsheet.css -f markdown-raw_html -t html -o cheatsheet.html")
	key(enter)
	sleep(1.5)
	user.add_links_to_cheatsheet()
	sleep(0.5)
	app.window_close()
show cheat sheet:
	key(super)
	sleep(0.2)
	insert("Anaconda")
	sleep(0.25)
	key(enter)
	sleep(2.5)
	insert("cd %appdata%/Talon/user/kronenfeld_talon/cheat sheet")
	key("enter")
	sleep(0.5)
	insert("python -m http.server 8080")
	sleep(0.5)
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


tab jiggle:
	key(tab)
	sleep(0.05)
	key(shift-tab)
ef six jiggle:
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
(switch|touch) (application|applications):
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
(delete|flick) way right:
	edit.extend_line_end()
	sleep(0.1)
	key(delete)
{user.search_engine} hunt:
	user.search_with_search_engine(search_engine, "")
	sleep(0.5)


stop: 
	user.mouse_scroll_stop()
	user.stop_repeating()
shutdown computer:
	key(super)
	sleep(0.2)
	key(up)
	sleep(0.2)
	key(right)
	key(enter)
	sleep(0.2)
	key(down:2)
	sleep(0.2)
	key(enter)
restart computer:
	key(super)
	sleep(0.2)
	key(up)
	sleep(0.2)
	key(right)
	key(enter)
	sleep(0.2)
	key(down:3)
	sleep(0.2)
	key(enter)

	
# key presses
# works in conjunction with the words to replace
press A:
	key(a)
press B:
	key(b)
press C:
	key(c)
press D:
	key(d)
press E:
	key(e)
press F:
	key(f)
press G:
	key(g)