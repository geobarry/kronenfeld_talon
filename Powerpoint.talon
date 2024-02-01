os: windows
and app.name: Microsoft PowerPoint
os: windows
and app.exe: POWERPNT.EXE
-
tag(): user.excel_powerpoint_shared
#main menu headings
menu file:
	key(alt-f)
menu home:
	key(alt-h)
menu insert:
	key(alt-n)
menu draw:
	key(alt-j)
	sleep(0.05)
	key(i)
menu design:
	key(alt-g)
menu (transition|transitions):
	key(alt-k)
menu (animation|animations):
	key(alt-a)
menu slide show:
	key(alt-s)
menu record:
	key(alt)
	sleep(0.05)
	key(c)
	key(1)
menu review:
	key(alt-r)
menu view:
	key(alt-w)
menu help:
	key(alt-h)
menu shape format:
	key(alt)
	sleep(0.05)
	key(j)
	key(d)
menu table design:
	key(alt)
	sleep(0.05)
	key(j)
	key(t)
menu table layout:
	key(alt)
	sleep(0.05)
	key(j)
	key(l)
menu picture format:
	key(alt)
	sleep(0.05)
	key(j)
	key(p)
menu graphics format:
	key(alt)
	sleep(0.05)
	key(j)
	key(g)
menu equation:
	key(alt)
	sleep(0.05)
	key(j)
	key(e)
menu video format:
	key(alt)
	sleep(0.1)
	key(j)
	key(p)
menu [video] playback:
	key(alt)
	sleep(0.1)
	key(j)
	key(n)

#file menu
save as:
	key(alt-f)
	sleep(0.05)
	key(a)
	sleep(0.5)
	key(o)

#home menu
(insert|new) slide:
	key(alt)
	sleep(0.2)
	key(h i)
slide layout:
	key(alt)
	sleep(0.2)
	key(h l)
font:
	key(alt)
	sleep(0.3)
	key(h f)
	key(f)
font size:
	key(alt)
	sleep(0.3)
	key(h f)
	key(s)
font size <number>:
	key(alt)
	sleep(0.3)
	key(h f)
	key(s)
	sleep(0.05)
	insert(number)
	sleep(0.05)
	key(enter)

	
font color:
	key(alt)
	sleep(0.4)
	key(h f)
	key(c)
font color red:
	key(alt)
	sleep(0.2)
	key(h f)
	key(c)
	key(down:6)
	key(enter)
font color black:
	key(alt)
	sleep(0.2)
	key(h f)
	key(c)
	key(right)
	key(enter)
font color teal:
	key(alt)
	sleep(0.2)
	key(h f)
	key(c)
	key(down:4)
	key(right:8)
	key(enter)

apply bold:
	key(alt)
	sleep(0.2)
	key(h 1)
apply (italic|italics):
	key(alt)
	sleep(0.2)
	key(h 2)
apply underline:
	key(alt)
	sleep(0.2)
	key(h 53)
apply subscript:
	key(alt-h)
	key(f)
	key(n)
	key(b)
	key(enter)
apply superscript:
	key(alt-h)
	key(f)
	key(n)
	key(p)
	key(enter)
apply bullets:
	key(alt)
	sleep(0.3)
	key(h u)
apply (default bullets|bullets default):
	key(alt)
	sleep(0.3)
	key(h u)
	key(left:12)
	key(right)
	key(enter)
apply numbers:
	key(alt)
	sleep(0.3)
	key(h n)
apply numbers [with] dots:
	key(alt)
	sleep(0.3)
	key(h n)
	key(left:12)
	key(right)
	key(enter)
apply numbers [with] parentheses:
	key(alt)
	sleep(0.3)
	key(h n)
	key(left:12)
	key(right:2)
	key(enter)
start [(numbers|numbering)] at <number>:
	key(alt)
	sleep(0.3)
	key(n n t)
	insert("{number}")
	key(enter)
	
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
[text] align left:
	key(alt-h)
	key(a)
	key(l)
[text] align center:
	key(alt-h)
	key(a)
	key(c)
[text] align right:
	key(alt-h)
	key(a)
	key(r)
[text] align top:
	key(alt-h)
	key(a)
	key(t)
	key(t)
[text] align middle:
	key(alt-h)
	key(a)
	key(t)
	key(m)
[text] align bottom:
	key(alt-h)
	key(a)
	key(t)
	key(b)
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
bring to front:
	key(alt)
	sleep(0.3)
	key(h g)
	key(r)
send to back:
	key(alt)
	sleep(0.3)
	key(h g)
	key(k)
rotate right:
	key(alt-h)
	sleep(0.05)
	key(g)
	key(o)
	key(r)
rotate left: 
	key(alt-h)
	sleep(0.05)
	key(g)
	key(o)
	key(l)
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
[insert] text box:
	key(alt-n)
	sleep(0.05)
	key(x)
	key(h)
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

insert shape:
	key(alt-n)
	sleep(0.05)
	key(s)
	key(h)
insert rectangle:
	key(alt-n)
	sleep(0.05)
	key(s)
	key(h)
	sleep(0.05)
	key(right:4)
	key(enter)

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
present slide show:
	key(alt-s)
	sleep(0.05)
	key(b)
present current slide:
	key(alt-s)
	sleep(0.05)
	key(c)

#view menu
slide sorter:
	key(alt-w)
	key(i)
outline view:
	key(alt-w)
	key(p)
	key(o)
normal view:
	key(alt-w)
	key(l)
(master view|slide master):
	key(alt-w)
	key(m)
rename [slide] layout:
	key(alt-m)
	key(r)
close (master [view]|slide master):
	key(alt-m)
	key(c)
	
zoom fit:
	key(alt-w)
	key(q)
	sleep(0.05)
	key(i)
	key(enter)
zoom <number> [percent]:
	key(alt-w)
	key(q)
	sleep(0.05)
	key(p)
	sleep(0.05)
	insert(number)
	insert("%")
	key(enter)

#shape format menu
[shape] format panel:
	key(menu)
	key(o)
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
	key(alt)
	sleep(0.05)
	key(j)
	key(d)
	key(s)
	sleep(0.05)
	key(f)	
	key(m)
	key(alt-t)
	insert(number)
	key(enter)
shape outline:
	key(alt)
	sleep(0.05)
	key(j)
	key(d)
	key(s)
	sleep(0.05)
	key(o)
shape no outline:
	key(alt)
	sleep(0.05)
	key(j)
	key(d)
	key(s)
	sleep(0.05)
	key(o)
	key(n)  
shape width:
	key(alt)
	sleep(0.08)
	key(j)
	key(d)
	key(w)
shape width <number>:
	key(alt)
	sleep(0.08)
	key(j)
	key(d)
	key(w)
	insert(number)
	key(enter)
	key(esc)
shape width <number> point <number>:
	key(alt)
	sleep(0.08)
	key(j)
	key(d)
	key(w)
	insert(number_1)
	insert(".")
	insert(number_2)
	key(enter)
	key(esc)
shape height:
	key(alt)
	sleep(0.08)
	key(j)
	key(d)
	key(h)
shape height <number>:
	key(alt)
	sleep(0.08)
	key(j)
	key(d)
	key(h)
	insert(number)
	key(enter)
	key(esc)
shape height <number> point <number>:
	key(alt)
	sleep(0.08)
	key(j)
	key(d)
	key(h)
	insert(number_1)
	insert(".")
	insert(number_2)
	key(enter)
	key(esc)
shape position:
	# first need to collapse all menus
	key(alt)
	sleep(0.08)
	key(j)
	key(d)
	key(s)
	key(z)
apply [text] halo:
	key(alt)
	sleep(0.2)
	key(j d t x g g c)

close panel:
	key(f6)
	key(ctrl-space)
	key(c)
exit panel:
	key(ctrl-space)
	key(c)

#table layout menu
insert row above:
	key(alt)
	sleep(0.08)
	key(j)
	key(l)
	key(v)
insert row below:
	key(alt)
	sleep(0.05)
	key(j)
	key(l)
	key(e)
insert column before:
	key(alt)
	sleep(0.05)
	key(j)
	key(l)
	key(l)
insert column after:
	key(alt)
	sleep(0.05)
	key(j)
	key(l)
	key(i)
delete row:
	key(alt)
	sleep(0.05)
	key(j)
	key(l)
	key(d)
	key(r)
delete column:
	key(alt)
	sleep(0.05)
	key(j)
	key(l)
	key(d)
	key(c)
delete table:
	key(alt)
	sleep(0.05)
	key(j)
	key(l)
	key(d)
	key(t)
(cell|column) width:
	key(alt)
	sleep(0.2)
	key(j)
	key(l)
	key(w)

	
# picture format menu
picture width:
	key(alt)
	sleep(0.08)
	key(j)
	key(p)
	key(w)
picture width <number>:
	key(alt)
	sleep(0.08)
	key(j)
	key(p)
	key(w)
	insert(number)
	key(enter)
	key(esc)
picture width <number> point <number>:
	key(alt)
	sleep(0.08)
	key(j)
	key(p)
	key(w)
	insert(number_1)
	insert(".")
	insert(number_2)
	key(enter)
picture height:
	key(alt)
	sleep(0.08)
	key(j)
	key(p)
	key(h)
picture height <number>:
	key(alt)
	sleep(0.08)
	key(j)
	key(p)
	key(h)
	insert(number)
	key(enter)
	key(esc)
picture height <number> point <number>:
	key(alt)
	sleep(0.08)
	key(j)
	key(p)
	key(h)
	insert(number_1)
	insert(".")
	insert(number_2)
	key(enter)
	key(esc)
picture position:
	# first need to collapse all menus
	key(alt)
	sleep(0.08)
	key(j)
	key(p)
	key(s)
	key(z)
crop [picture]:
	key(alt)
	sleep(0.08)
	key(j)
	key(p)
	key(v)
	key(c)
[picture] transparent color:
	key(alt)
	sleep(0.08)
	key(j)
	key(p)
	key(i)
	key(s)


graphics width:
	key(alt)
	sleep(0.08)
	key(j)
	key(g)
	key(w)
graphics width <number>:
	key(alt)
	sleep(0.08)
	key(j)
	key(g)
	key(w)
	insert(number)
	key(enter)
	key(esc)
graphics width <number> point <number>:
	key(alt)
	sleep(0.08)
	key(j)
	key(g)
	key(w)
	insert(number_1)
	insert(".")
	insert(number_2)
	key(enter)
graphics height:
	key(alt)
	sleep(0.08)
	key(j)
	key(g)
	key(h)
graphics height <number>:
	key(alt)
	sleep(0.08)
	key(j)
	key(g)
	key(h)
	insert(number)
	key(enter)
graphics height <number> point <number>:
	key(alt)
	sleep(0.08)
	key(j)
	key(g)
	key(h)
	insert(number_1)
	insert(".")
	insert(number_2)
	key(enter)
graphics position:
	# first need to collapse all menus
	key(alt)
	sleep(0.08)
	key(j)
	key(g)
	key(s)
	key(z)



#equation menu
insert fraction:
	key(alt)
	sleep(0.05)
	key(j)
	key(e)
	key(f)
insert script:
	key(alt)
	sleep(0.05)
	key(j)
	key(e)
	key(s)
insert radical:
	key(alt)
	sleep(0.05)
	key(j)
	key(e)
	key(r)
insert large operator:
	key(alt)
	sleep(0.05)
	key(j)
	key(e)
	key(g)
equation insert symbol:
	key(alt)
	sleep(0.05)
	key(j)
	key(e)
	key(q)
insert accent:
	key(alt)
	sleep(0.05)
	key(j)
	key(e)
	sleep(0.05)
	key(a)
[insert] accent bar:
	key(alt)
	sleep(0.1)
	key(j)
	key(e)
	sleep(0.05)
	key(a)
	key(left:99)
	key(right:9)
	key(enter)
	key(left)

# playback menu
update timing:
	# updates transition timing to length of selected video
	key(alt)
	sleep(0.3)
	key(j)
	key(n)
	key(t)
	sleep(0.1)
	key(alt-e)
	edit.copy()
	key(tab)
	key(enter)
	key(alt)
	sleep(0.1)
	key(k)
	key(i)
	edit.paste()
	key(enter)
	key(esc)
	

# common operations	
copy style:
	key(ctrl-shift-c)
paste style:
	key(ctrl-shift-v)
paste special:
	key(alt)
	sleep(0.2)
	key(h v s tab)
paste without formatting:
	key(alt-e)
	sleep(0.05)
	key(s)
	key(tab)
	key(down:2)
	key(enter)

#special symbols
insert greek [letter]:
	key(alt-n)
	key(u)
	key(alt-f)
	insert("Times New Roman")
	sleep(0.1)
	key(enter)
	key(alt-m)
	key(up:2)
	key(enter)
	key(alt-c)
	key(shift-tab:2)

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