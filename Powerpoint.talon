os: windows
and app.name: Microsoft PowerPoint
os: windows
and app.exe: POWERPNT.EXE
-
tag(): user.excel_powerpoint_shared

# experimental accessibility

toggle notes: user.focus_element_by_name("notes")
focus workspace: user.click_element_by_name("home")
mark for selection: user.mark_focused_location()
select marked: 
	key(esc)
	user.click_all_marks("shift")
go to {user.power_go_to_target}: user.power_go_to(power_go_to_target)
select [<user.ordinals>] {user.power_selection_target}: user.power_tab_to(power_selection_target,ordinals or 1)
select inside [<user.ordinals>] {user.power_selection_target}:
	user.power_tab_to(power_selection_target,ordinals or 1)
	sleep(0.2)
	key("f2")

go to slide <number>: user.power_go_to_slide(number)

#main menu headings
menu file: key(alt-f)
menu home: key(alt-h)
menu insert: key(alt-n)
menu draw: key(alt j i)
menu design: key(alt-g)
menu (transition|transitions): key(alt-k)
menu (animation|animations): key(alt-a)
menu slide show: key(alt-s)
menu record: key(alt c 1)
menu review: key(alt-r)
menu view: key(alt-w)
menu help: key(alt-h)
menu shape format: key(alt j d)
menu table design: key(alt j t)
menu table layout: key(alt j l)
menu picture format: key(alt j p)
menu graphics format: key(alt j g)
menu equation: key(alt j e)
menu video format: key(alt j p)
menu [video] playback: key(alt j n)
menu slide master: key(alt m)

menu object: user.power_object_menu()

#file menu
save file as: 
	key(alt f a)
	sleep(0.5)
	key(o)

#home menu
(insert|new) slide: key(alt h i)
slide layout: key(alt h l)
font: key(alt h f:2)
font size: key(alt h f s)
font size <number>:
	key(alt h f s)
	sleep(0.05)
	insert(number)
	sleep(0.05)
	key(enter)
font color: key(alt-h f c)
font color white: key(alt h f c enter)
font color standard: key(alt h f c home tab:2)
font color red: key(alt h f c home tab:2 enter)
font color black: key(alt h f c home right enter)
font color teal: key(alt h f c down:4 right:8 enter)
font color recent: key(alt h f c home tab:3)
font color same as last: key(alt h f c home tab:3 enter)

apply bold: key(alt h 1)
apply (italic|italics): key(alt h 2)
apply underline: key(alt h 3)
apply strike through: key(alt-h 4) 
apply subscript: key(alt-h f n b enter)
apply superscript: key(alt-h f n p enter)
apply bullets:key(alt h u)
apply bullets none: key(alt h u home enter)
apply bullets [filled] round:
	key(alt h u home)
	user.key_to_elem_by_val("right","Filled Round Bullets")
	key(enter)
apply (default bullets|bullets default): key(alt h u home right enter)
apply numbers: key(alt h n)
apply numbers [with] dots:
	key(alt h n home)
	user.key_to_elem_by_val("right", "1. 2. 3.")
	key(enter)
apply numbers [with] (parentheses|parents):
	key(alt h n home)
	user.key_to_elem_by_val("right", "1) 2) 3)")
	key(enter)
apply letters [lowercase] [with] (parentheses|parents):
	key(alt h n home)
	user.key_to_elem_by_val("right", "a) b) c)")
	key(enter)
apply letters [lowercase] [with] dots:
	key(alt h n home)
	user.key_to_elem_by_val("right", "a. b. c.")
	key(enter)
apply letters (uppercase|capital) [with] dots:
	key(alt h n home)
	user.key_to_elem_by_val("right", "A. B. C.")
	key(enter)
		
(start|restart) [(numbers|numbering)] at <number>:
	key(alt h n:2 t)
	insert("{number}")
	key(enter)
apply last highlight: user.slow_key_press("alt h t c down:3 enter")	
paragraph formatting:
	key(alt)
	sleep(0.3)
	key(h p g)
	
(indent|demote):
	key(alt)
	sleep(0.2)
	key(h)
	sleep(0.2)
	key(z p a i)
(dedent|promote):
	key(alt)
	sleep(0.3)
	key(h z p a o)
[text] align left: key(alt-h a l)
[text] align center: key(alt-h a c)
[text] align right: key(alt-h a r)
[text] align top: key(alt-h a t:2)
[text] align middle: key(alt-h a t m)
[text] align bottom: key(alt-h a t b)
clear (fill|fell|feel):
	key(alt-h)
	sleep(0.05)
	key(s)
	key(f)
	key(n)
fill color:
	key(alt-h)
	sleep(0.05)
	key(s)
	key(f)
	key(down:6)
fill transparent:
	key(alt-h)
	sleep(0.05)
	key(s)
	key(f)
	key(n)
outline color:
	key(alt-h)
	sleep(0.05)
	key(s)
	key(o)
	key(down:6)
outline [color] red:
	key(alt-h)
	sleep(0.05)
	key(s)
	key(o)
	key(down:6)
	key(right)
	key(enter)
outline width:
	key(alt-h)
	sleep(0.05)
	key(s)
	key(o)
	key(w)
outline width one:
	key(alt-h)
	sleep(0.05)
	key(s)
	key(o)
	key(w)
	sleep(0.9)
	key(down:3)
	sleep(0.1)
	key(enter)
outline width three:
	key(alt)
	sleep(0.3)
	key(h s)
	key(o)
	key(w)
	sleep(0.9)
	key(down:6)
	sleep(0.1)
	key(enter)
outline style:
	key(alt)
	sleep(0.3)
	key(h s o)
bring to front: key(alt-h g r)
send to back: key(alt-h g k)
align (objects|edges) left: key(alt-h g a l)
align (objects|edges) right: key(alt-h g a r)
align (objects|edges) top: key(alt-h g a t)
align (objects|edges) bottom: key(alt-h g a b)
align (objects|edges) middle: key(alt-h g a m)
align (objects|edges) center: key(alt-h g a c)
distribute horizontal: key(alt-h g a h)
distribute vertical: key(alt-h g a v)
rotate clockwise: key(alt h g o r)
rotate counterclockwise: key(alt-h g o l)
rotate right: key(alt-right)
rotate tiny right: key(ctrl-alt-right)
rotate left: key(alt-left)
rotate tiny left: key(ctrl-alt-left)
flip vertical:
	key(alt-h)
	sleep(0.05)
	key(g)
	key(o)
	key(v)
flip horizontal:
	key(alt-h)
	sleep(0.05)
	key(g)
	key(o)
	key(h)
	
#insert menu
[(place|insert)] text box: 
	user.slow_key_press("alt n x h esc alt j d w 5 shift-tab 1 enter esc f2")
insert [hyper] link:
	key(alt-n)
	sleep(0.05)
	key(z)
	key(l)
	key(i:2)
insert icon:
	key(alt-n)
	sleep(0.05)
	key(n)
	key(s)
	sleep(0.5)

insert shape: key(alt-n s h)
insert rectangle:
	key(alt-n s h)
	sleep(0.05)
	key(right:4 enter)
insert table: key(alt-n t)
[insert] rounded rectangle:
	key(alt-n)
	sleep(0.05)
	key(s)
	key(h)
	sleep(0.05)
	key(right:6)
	key(enter)
insert Bezier curve:
	key(alt-n)
	sleep(0.05)
	key(s)
	key(h)
	sleep(0.05)
	key(down)
	key(enter)
	
insert equation:
	key(alt-n)
	sleep(0.05)
	key(e)
	sleep(0.05)
	key(i)

#record menu
record current slide:
	key(alt-c)
	sleep(0.05)
	key(c)
	key(s)
	user.activate_power_recording()
record screen:
	key(alt-c)
	sleep(0.05)
	key(r)
	key(1)
	user.activate_power_screen_recording()
insert cameo:
	key(alt-c)
	sleep(0.05)
	key(c)
	key(1)

# transitions menu ribbon shortcuts
clear (transition|timing):
	key(alt-k)
	key(i)
	insert("0")
	key(enter)
	key(esc)

#animation ribbon shortcuts
apply animation:
	key(alt-a)
	key(s)
	key(pageup:3)

apply animation fade:
	key(alt-a)
	key(s)
	key(pageup:3)
	key(down)
	key(right)
	key(enter)
apply animation appear:
	key(alt-a)
	key(s)
	key(pageup:3)
	key(down)
	key(enter)
apply animation wipe [right]:
	key(alt-a)
	key(s)
	key(pageup:3)
	key(down)
	key(right:5)
	key(enter)
	key(alt-a)
	key(o)
	key(l)
animation panel:
	key(alt-a)
	key(c)
exit animation panel:
	key(esc)
	key(alt-a)
	key(c)
	
#slide show menu
present slide show: key(alt s b)
present current slide: key(alt s c)

#view menu
slide sorter: key(alt w i)
outline view: key(alt w p o)
normal view: key(alt w l)
(master view|slide master): key(alt w m)
rename [slide] layout: key(alt m r)
close (master [view]|slide master): key(alt m c)
zoom fit: key(alt w q i enter)
zoom <number> [percent]:
	key(alt w q p)
	insert("{number}%")
	key(enter)

#shape format menu
[shape] format panel: key(menu o)
position:
	key(menu o)
	user.power_tab_format_panel_top_row()
	user.key_to_elem_by_val("right","Size & Properties")
	user.key_to_elem_by_val("tab","Position")
	user.toggle_for_next_value("Horizontal position","enter")
	key(tab)
position top:
	key(menu o)
	user.power_tab_format_panel_top_row()
	user.key_to_elem_by_val("right","Size & Properties")
	user.key_to_elem_by_val("tab","Position")
	user.toggle_for_next_value("Horizontal position","enter")
	key(tab:3)
position top <user.real_number>:
	key(menu o)
	user.power_tab_format_panel_top_row()
	user.key_to_elem_by_val("right","Size & Properties")
	user.key_to_elem_by_val("tab","Position")
	user.toggle_for_next_value("Horizontal position","enter")
	key(tab:3)
	insert("{real_number}")
	key(enter ctrl-space c)
position left:
	key(menu o)
	user.power_tab_format_panel_top_row()
	user.key_to_elem_by_val("right","Size & Properties")
	user.key_to_elem_by_val("tab","Position")
	user.toggle_for_next_value("Horizontal position","enter")
	key(tab)
position left <user.real_number>:
	key(menu o)
	user.power_tab_format_panel_top_row()
	user.key_to_elem_by_val("right","Size & Properties")
	user.key_to_elem_by_val("tab","Position")
	user.toggle_for_next_value("Horizontal position","enter")
	key(tab)
	insert("{real_number}")
	key(enter ctrl-space c)
toggle aspect ratio:
	key(menu o)
	user.power_tab_format_panel_top_row()
	user.key_to_elem_by_val("right","Size & Properties")
	user.key_to_elem_by_val("tab","Size")
	user.toggle_for_next_value("Height","enter")
	key(a)
	# sleep a little to make sure user can see the toggled state
	sleep(0.7)
	key(enter ctrl-space c)

shape fill:
	key(alt)
	sleep(0.05)
	key(j)
	key(d)
	key(s)
	sleep(0.05)
	key(f)
shape [fill] transparency:
	key(alt)
	sleep(0.05)
	key(j)
	key(d)
	key(s)
	sleep(0.05)
	key(f)	
	key(m)
	key(alt-t)
shape [fill] transparency <number>:
	key(alt j d s)
	sleep(0.05)
	key(f m alt-t)
	insert(number)
	key(enter)
shape outline:
	key(alt j d s)
	sleep(0.05)
	key(o)
shape no outline:
	key(alt j d s)
	sleep(0.05)
	key(o n)
shape width: user.office_keys("alt j d w")
shape width <user.real_number>:
	user.office_keys("alt j d w")
	insert("{real_number}")
	key(enter esc)
picture width: user.office_keys("alt j p w")
picture width <user.real_number>:
	user.office_keys("alt j p w")
	insert("{real_number}")
	key(enter esc)
shape height: key(alt j d h)
shape height <user.real_number>:
	key(alt j d h)
	insert(real_number)
	key(enter esc)
shape position: user.office_keys("alt j d s z")
apply [text] halo: user.office_keys("alt j d t x g g c")
close panel: key(f6 ctrl-space c)
exit panel: key(ctrl-space c)

#table layout menu
insert row [above]: user.office_keys("alt j l v")
insert row below: user.office_keys("alt j l e")
insert column [before]: user.office_keys("alt j l l")
insert column after: user.office_keys("alt j l i")
delete row: user.office_keys("alt j l d r")
delete column: user.office_keys("alt j l d c")
delete table: user.office_keys("alt j l d t")
(cell|column) width: user.office_keys("alt j l w")
table width: user.slow_key_press("alt j l t w")
table height: user.slow_key_press("alt j l t h")
	
# picture format menu

picture height:
	key(alt)
	sleep(0.08)
	key(j)
	key(p)
	key(h)
picture height <number>:
	key(alt j p h)
	insert(number)
	key(enter esc)
picture height <number> point <number>:
	key(alt j p h)
	insert("{number_1}.{number_2}")
	key(enter esc)
picture position: key(alt j p s z)
crop picture: user.power_crop_picture("upper left")
crop {user.handle_position}: user.power_crop_picture(handle_position)
[picture] transparent color: key(alt j p i s)
picture border black: user.slow_key_press("alt j p s o enter")

graphics width: key(alt j g w)
graphics width <number>:
	key(alt j g w)
	insert(number)
	key(enter esc)
graphics width <number> point <number>:
	key(alt j g w)
	insert("{number_1}.{number_2}")
	key(enter esc)
graphics height: key(alt j g h)
graphics height <number>:
	key(alt j g h)
	insert(number)
	key(enter esc)
graphics height <number> point <number>:
	key(alt j g h)
	insert("{number_1}.{number_2}")
	key(enter esc)
graphics position:
	key(alt j g s z)

#equation menu
equation fraction: key(alt j e f)
equation script: key(alt j e s)
equation radical: key(alt j e r)
equation large operator: key(alt j e g)
equation symbol: key(alt j e q) 
equation accent: key(alt j e a)
[equation] accent bar: key(alt j e a left:99 right:9 enter left)

# playback menu
update timing:
	# updates transition timing to length of selected video
	key(alt j n t)
	sleep(0.1)
	key(alt-e)
	edit.copy()
	key(tab enter alt)
	sleep(0.1)
	key(k i)
	edit.paste()
	key(enter esc)

# common operations	
copy style: key(ctrl-shift-c)
paste style: key(ctrl-shift-v)
paste special: user.office_keys("alt h v s tab")
paste without formatting: user.office_keys("alt-e s tab down:2 enter")
paste original formatting: user.office_keys("alt-h v k")

#special symbols
insert greek [letter]:
	key(alt n u alt-f)
	insert("Times New Roman")
	sleep(0.1)
	key(enter alt-m up:2 enter alt-c shift-tab:2)

# hacks for aligning objects
duplicate right:
	# first zoom to 82% so that this works
	key(alt-w)
	key(q)
	sleep(0.05)
	key(p)
	sleep(0.05)
	insert(82)
	insert("%")
	key(enter)
	sleep(0.5)
	# duplicate object
	key(ctrl-d)
	# move up to align
	key(up:11)

duplicate small right:
	# first zoom to 82% so that this works
	key(alt-w)
	key(q)
	sleep(0.05)
	key(p)
	sleep(0.05)
	insert(82)
	insert("%")
	key(enter)
	sleep(0.5)
	# duplicate object
	key(ctrl-d)
	# move up to align
	key(up:11)
	# move right
	key(right:5)
	# Why does this do weird things when you try to repeat?
	
close [designer] panel:
	key(f6)
	key(ctrl-space)
	key(c)