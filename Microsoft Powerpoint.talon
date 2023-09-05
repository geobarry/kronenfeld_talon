os: windows
and app.name: Microsoft PowerPoint
os: windows
and app.exe: POWERPNT.EXE
-
#main menu headings
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
	key(alt-c)
menu review:
	key(alt-r)
menu view:
	key(alt-w)
menu help:
	key(alt-h)
menu shape format:
	key(alt-j)
	sleep(0.05)
	key(d)
menu table design:
	key(alt-j)
	sleep(0.05)
	key(t)
menu table layout:
	key(alt-j)
	sleep(0.05)
	key(l)
menu equation:
	key(alt-j)
	sleep(0.05)
	key(e)
menu picture format:
	key(alt-j)
	sleep(0.05)
	key(p)

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
	insert({number})
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
clear (fill|fell|feel):
	key(alt-h)
	sleep(0.05)
	key(s)
	key(f)
	key(n)
	
#insert menu
text box:
	key(alt-n)
	sleep(0.05)
	key(x)
	key(h)

#slide show menu
present slide show:
	key(alt-s)
	sleep(0.05)
	key(b)
key(w):
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
slide master:
	key(alt-w)
	key(m)
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
	key(alt-j)
	sleep(0.05)
	key(d)
	key(s)
	sleep(0.05)
	key(o)

	
# common operations	
copy style:
	key(ctrl-shift-c)
paste style:
	key(ctrl-shift-v)
