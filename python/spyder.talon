os: windows
and app.name: Python
os: windows
and app.exe: pythonw.exe

-
tag(): user.my_python

tab previous: key(ctrl-pageup)
tab next: key(ctrl-pagedown)
tab close: key(ctrl-w)

save as: key(ctrl-shift-s)

# focus on a particular pane
[focus] panel code: key(alt-v enter:2 alt-v enter:2)
focus panel {user.spyder_panel}: user.spyder_focus_panel("{spyder_panel}")
close panel {user.spyder_panel}: user.spyder_close_panel("{spyder_panel}")
[open] panel {user.spyder_panel}: user.spyder_open_panel("{spyder_panel}")

# auto captures
capture modules: user.spyder_capture_module_names()
capture functions: user.spyder_capture_function_names()

# module navigation
open module {user.module_list}: user.spyder_open_module(module_list)
close module {user.module_list}:
	user.spyder_open_module(module_list)
	sleep(0.3)
	key(ctrl-w)
go to function {user.function_list}: user.spyder_go_to_function(function_list)
test open module: user.spyder_test_open_module()

clear (plot|plots):
	key(ctrl-shift-g)
    user.mouse_helper_position_save()
    user.mouse_helper_move_image_relative("spyder_hamburger_right_pane.png", 0, -50, 70)
    sleep(0.5)
    mouse_click(0)
    sleep(0.75)
	key(ctrl-shift-w)
clear (console|interpreter): key(ctrl-shift-i ctrl-l)
(next|change) layout: key(alt-shift-pagedown)
check error:
    user.mouse_helper_position_save()
    user.mouse_helper_move_image_relative("spyder_error_mark.png", 0, 0, 0)
    sleep(0.05)
    mouse_click(0)
    sleep(0.05)
    #user.mouse_helper_position_restore()
go [to line] <number>:
	key(esc ctrl-l)
	sleep(0.1)
	insert("{number}")
	key(enter)
go to line:	key(esc ctrl-l)
select [lines] <number> through <number>: user.spyder_select_lines(number_1,number_2)
select <number>: user.spyder_select_lines(number,number)
maximize pane: key(ctrl-alt-shift-m)
format out:
	insert('{}')
	edit.right()
	insert('.format()')
	edit.left()
format <number> decimal places:
	insert("{:.")
	insert(number_1)
	insert("f}")
run code: key(f5)
debug: key(ctrl-f5)
step: key(ctrl-f10)
step into: key(ctrl-f11)
continue: key(ctrl-f12)
stop code: key(ctrl-shift-f12)
toggle breakpoint: key(f12)
(toggle) comment$: key(ctrl-1)
comment <user.text>: insert("# {text}")
doc string: 
	key('" " "')
	sleep(0.8)
	key(enter)
go to definition: key(ctrl-g)
# splitter
split left: user.spyder_move_split("left")
split left <number>: user.spyder_move_split("left",number)
split right: user.spyder_move_split("right")
split right <number>: user.spyder_move_split("right",number)


# menus
file menu: key(alt-f)
edit menu: key(alt-e)
search menu: key(alt-s)
source menu: key(alt-c)
run menu: key(alt-r)
debug menu: key(alt-d)
(console|consoles) menu: key(alt-o)
(project|projects) menu: key(alt-p)
(tool|tools) menu: key(alt-t)
view menu: key(alt-v)
help menu: key(alt-h)
	
# Project menu shortcuts
open project: user.slow_key_press("alt-p down enter",0.5)