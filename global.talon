os: windows
-
# disabling talon
hello hello: speech.disable()
hello come [on] in$: speech.disable()
hello what's up: speech.disable()
computer [go to] sleep: speech.disable()
computer stop listening: speech.disable()
computer close your ears: speech.disable()

# modes
mixed mode:
	# Why isn't this working????
	mode.disable("sleep")
	mode.disable("dictation")
	mode.disable("command")
	mode.enable("mixed")
	

# windows volume
volume up: key(volup)
volume down: key(voldown)
volume mute: key(mute)

# windows keyboard shortcuts
launch explorer: key(super-e)
screen snip: 
	sleep(5)
	key(super-shift-s)
go to Bluetooth:
	key(super-a)
	sleep(1)
	key(right)
	sleep(0.5)
	key(tab enter)

toggle Bluetooth: 
	key(super-a)
	sleep(1)
	key(right)
	sleep(0.5)
	key(tab enter)
	sleep(0.7)
	key(space esc)	

# FOCUS
refocus: user.slow_key_press("alt:down tab left alt:up",0.1)
# special command to focus on an explorer windows since windows has so many
focus explorer: user.focus_explorer()
		
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
open up <user.real_number>:
	insert("{real_number}")
	sleep(0.15)
	key(enter)
open up {user.abbreviation}:
	insert("{abbreviation}")
	sleep(0.05)
	key(enter)

# NUMBERS
real <user.real_number>:
	insert("{real_number}")
	


# COMMON WORDS
my [full] name: insert("Barry Kronenfeld")
my first name: insert("Barry")
my last name: insert("Kronenfeld")
	
my gmail: insert("barrykronenfeld@gmail.com")
my email: insert("bjkronenfeld@eiu.edu")
dotcom: insert(".com")
daddy to you: insert(".edu")
dot education: insert(".edu")
dot gove: insert(".gov")
dot python: insert(".py")
dot iron python notebook: insert(".ipynb")

inside inches: user.insert_between('"', '"')
inside feet: user.insert_between("'", "'")

double brief {user.abbreviation} {user.abbreviation}: "{abbreviation} {abbreviation_2}"
double under brief {user.abbreviation} {user.abbreviation}: "{abbreviation}_{abbreviation_2}"

(numb|number|numeral) <number>: insert("{number}")
# letter <user.letter>: insert("{letter}")

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
	
modify text: key(f2)

undo$: key(ctrl-z)
redo$: key(ctrl-y)
focus taskbar: key(super-b)
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

hold down shift: key(shift:down)
hold down control: key(ctrl:down)
hold down (alt|alternate): key(alt:down)
release keys: key(shift:up ctrl:up alt:up super:up)
escape out: key(esc:5)
shift click: 
	key(shift:down)
	mouse_click(0)
	key(shift:up)

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



stop [it]: 
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

	
