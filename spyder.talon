app.name: Python
-
tag(): user.python
tag(): user.line_commands
# focus on the code window
focus code:
	key(alt-v)
	key(enter)
	key(enter)
	key(alt-v)
	key(enter)
	key(enter)
focus outline:
	key(ctrl-shift-o)
    user.mouse_helper_position_save()
    user.mouse_helper_move_image_relative("spyder_hamburger_right_pane.png", 0, -50, 70)
    sleep(0.3)
    mouse_click(0)
tab previous:
	key(ctrl-pageup)
tab next:
	key(ctrl-pagedown)
tab close:
	key(ctrl-w)
focus (variable|variables):
	key(ctrl-shift-v)
focus (interpreter|console):
	key(ctrl-shift-i)
focus project:
	key(ctrl-shift-p)
    user.mouse_helper_position_save()
    user.mouse_helper_move_image_relative("spyder_hamburger_right_pane.png", 0, -50, 70)
    sleep(0.05)
    mouse_click(0)
    sleep(0.05)
    #user.mouse_helper_position_restore()
focus (plot|plots):
	key(ctrl-shift-g)
    user.mouse_helper_position_save()
    user.mouse_helper_move_image_relative("spyder_hamburger_right_pane.png", 0, -50, 70)
    sleep(0.05)
    mouse_click(0)
    sleep(0.05)
    #user.mouse_helper_position_restore()

clear (plot|plots):
	key(ctrl-shift-g)
    user.mouse_helper_position_save()
    user.mouse_helper_move_image_relative("spyder_hamburger_right_pane.png", 0, -50, 70)
    sleep(0.5)
    mouse_click(0)
    sleep(0.75)
	key(ctrl-shift-w)
clear (console|interpreter):
	key(ctrl-shift-i)
	key(ctrl-l)
(next|change) layout:
	key(alt-shift-pagedown)
check error:
    user.mouse_helper_position_save()
    user.mouse_helper_move_image_relative("spyder_error_mark.png", 0, 0, 0)
    sleep(0.05)
    mouse_click(0)
    sleep(0.05)
    #user.mouse_helper_position_restore()
go to line <number>:
	key(esc)
	key(ctrl-l)
	sleep(0.1)
	insert("{number}")
	key(enter)
go to line:
	key(esc)
	key(ctrl-l)
debug print :
	insert('print("')
maximize pane:
	key(ctrl-alt-shift-m)
format out:
	insert('{}')
	edit.right()
	insert('.format()')
	edit.left()
format <number> decimal places:
	insert("{:.")
	insert(number_1)
	insert("f}")
run code:
	key(f5)
debug:
	key(ctrl-f5)
step:
	key(ctrl-f10)
step into:
	key(ctrl-f11)
continue:
	key(ctrl-f12)
stop code:
	key(ctrl-shift-f12)
toggle breakpoint:
	key(f12)
toggle comment: 
	key(ctrl-1)