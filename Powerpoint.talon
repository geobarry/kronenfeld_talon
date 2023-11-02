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

#file menu
save as:
	key(alt-f)
	sleep(0.05)
	key(a)
	sleep(0.5)
	key(o)

#home menu
new slide:
	key(alt-h)
	sleep(0.05)
	key(i)
slide layout:
	key(alt-h)
	sleep(0.05)
	key(l)
font:
	key(alt-h)
	sleep(0.05)
	key(f)
	key(f)
font size:
	key(alt-h)
	key(f)
	key(s)
font size <number>:
	key(alt-h)
	sleep(0.05)
	key(f)
	key(s)
	sleep(0.05)
	insert(number)
	sleep(0.05)
	key(enter)
font color:
	key(alt-h)
	sleep(0.05)
	key(f)
	key(c)
apply bold:
	key(alt-h)
	key(1)
apply (italic|italics):
	key(alt-h)
	key(2)
apply underline:
	key(alt-h)
	key(3)
indent:
	key(alt-h)
	key(a)
	key(i)
dedent:
	key(alt-h)
	key(a)
	key(o)
clear (fill|fell|feel):
	key(alt-h)
	sleep(0.05)
	key(s)
	key(f)
	key(n)
send to back:
	key(alt-h)
	sleep(0.05)
	key(g)
	key(k)
	
#insert menu
text box:
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

#animation ribbon shortcuts
apply animation [fade]:
	key(alt-a)
	key(s)
	key(down)
	key(right)
	key(enter)
#animation ribbon shortcuts
apply animation appear:
	key(alt-a)
	key(s)
	key(down)
	key(enter)
	
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
close (master view|slide master):
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
shape fill:
	key(alt-j)
	sleep(0.05)
	key(d)
	key(s)
	sleep(0.05)
	key(f)
shape outline:
	key(alt)
	sleep(0.05)
	key(j)
	key(d)
	key(s)
	sleep(0.05)
	key(o)

#equation menu
	
# common operations	
copy style:
	key(ctrl-shift-c)
paste style:
	key(ctrl-shift-v)
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