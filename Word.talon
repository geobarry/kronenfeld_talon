app: Microsoft Word

-
sub <user.letter>:
	insert(" ")
	edit.left()
	key(alt-h)
	key(5)
	insert("{user.letter}")
	key(alt-h)
	key(5)
	edit.right()
	
sub <number>:
	insert(" ")
	edit.left()
	key(alt-h)
	key(5)
	insert("{number}")
	key(alt-h)
	key(5)
	edit.right()
	
apply style:
	key(alt-h)
	key(z)
	key(1)
	key(y)
	key(1)

new style:
	key(alt-h)
	key(f)
	key(y)
	sleep(0.05)
	# trick: if we press right enough times we will always end up in the same place
    key(right:10)
	# tab to the ad style button
	key(tab:3)
	key(enter)
	
apply heading <number>:
	key(alt-h)
	key(z)
	key(1)
	key(y)
	key(1)
	sleep(0.05)
	insert("Heading ")
	insert("{number}")
	key(enter)
	key(esc)
	repeat(4)

apply normal:
	key(alt-h)
	key(z)
	key(1)
	key(y)
	key(1)
	sleep(0.05)
	insert("normal")
	key(enter)
	key(esc)
	repeat(4)
	
apply code:
	key(alt-h)
	key(z)
	key(1)
	key(y)
	key(1)
	sleep(0.05)
	insert("Code")
	key(enter)
	key(esc)
	repeat(4)
	
apply code in place:
	key(alt-h)
	key(z)
	key(1)
	key(y)
	key(1)
	sleep(0.05)
	insert("Inline Code")
	key(enter)
	key(esc)
	repeat(4)
	
style match selection:
	key(alt-h)
	sleep(0.05)
	key(f)
	key(y)
	sleep(0.05)
	# trick: if we press right enough times we will always end up in the same place
	key(right:2)
	sleep(0.05)
	key(alt-down)
	sleep(0.05)
	key(enter)
	sleep(0.05)
	key(alt-h)
	key(f)
	key(y)

figure <number> here:
	insert("<figure ")
	insert("{number}")
	insert(" approximately here>")

table <number> here:
	insert("<table ")
	insert("{number}")
	insert(" approximately here>")
	
apply bullets:
	key(alt-h)
	key(u)
	key(right)
apply (numbering|numbers):
	key(alt-h)
	key(n)
	key(right)
restart (numbering|numbers):
	key(esc)
	key(esc)
	key(esc)
	key(esc)
	key(esc)
	key(alt-h)
	key(n)
	key(v)
	key(alt-v)
	sleep(0.05)
	key(1)
	key(enter)

save as:
	key(alt-f)
	sleep(0.05)
	key(a)
	
menu view:
	key(alt-w)
menu file:
	key(alt-f)
menu home:
	key(alt-h)	
menu insert:
	key(alt-n)
menu draw:
	key(alt-j)
	key(i)
menu design:
	key(alt-g)	
menu layout:
	key(alt-p)	
menu references:
	key(alt-s)
menu review:
	key(alt-r)
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
	sleep(0.05)
	key(p)
menu equation:
	key(alt)
	sleep(0.2)
	key(j)
	key(e)


#file ribbon shortcuts
export to PDF:
	key(alt-f)
	key(e)
	key(a)

#home ribbon shortcuts
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
paragraph formatting:
	key(alt-h)
	sleep(0.05)
	key(p)
	key(g)
apply bold:
	key(alt-h)
	key(1)
apply (italic|italics):
	key(alt-h)
	key(2)
apply underline:
	key(alt-h)
	key(3)

# insert menu shortcuts
insert table:
	key(alt-n)
	key(t)
insert comment:
	key(alt-n)
	key(l)
	
#edit ribbon shortcuts
paste without formatting:
	key(alt-e)
	sleep(0.05)
	key(s)
	sleep(0.15)
	key(a)
	sleep(.75)
	key(u)
	sleep(0.15)
	key(enter)

#view ribbon shortcuts
zoom fit [(width|with)]:
	key(alt-w)
	sleep(0.1)
	key(q)
	sleep(0.1)
	key(p)
	sleep(0.1)
	key(enter)
zoom [fit] text:
	key(alt-w)
	sleep(0.1)
	key(q)
	sleep(0.05)
	key(t)
	key(enter)
zoom [fit] page:
	key(alt-w)
	sleep(0.1)
	key(q)
	sleep(0.05)
	key(w)
	key(enter)
zoom <number> [percent]:
	key(alt-w)
	sleep(0.1)
	key(q)
	sleep(0.1)
	key(e)
	sleep(0.1)
	insert(number)
	insert("%")
	key(enter)

#menu table layout 
insert row [above]:
	key(alt)
	key(j)
	sleep(0.2)
	key(l)
	key(a)
insert [row] below:
	key(alt)
	key(j)
	sleep(0.2)
	key(l)
	key(b)
	key(e)
delete row:
	key(alt)
	key(j)
	sleep(0.2)
	key(l)
	key(d)
	key(r)
delete column:
	key(alt)
	key(j)
	sleep(0.2)
	key(l)
	key(d)
	key(c)
column (with|width):
	key(alt)
	sleep(0.2)
	key(j)
	sleep(0.2)
	key(l)
	key(w)

# common operations	
copy style:
	key(ctrl-shift-c)
paste style:
	key(ctrl-shift-v)
underline [that]:
	key(ctrl-u)

view text width:
	key(alt-w)
	sleep(0.15)
	key(q)
	key(alt-t)
	key(enter)	
# center on screen by toggling between webview and print view
# strangely this doesn't work when we put the two key sequences together
view webpage:
	key(alt)
	key(w)
	sleep(0.25)
	key(l)
	key(1)
view print:
	key(alt-w)
	sleep(0.15)
	key(p)
	
view page width:
	key(alt-w)
	sleep(0.15)
	key(q)
	key(alt-p)
	key(enter)
view whole page:
	key(alt-w)
	sleep(0.15)
	key(q)
	key(alt-w)
	key(enter)
view percent:
	key(alt-w)
	sleep(0.15)
	key(q)
	key(alt-e)
	key(enter)
	
export styles:
	key(alt-h)
	key(f)
	key(y)
	sleep(0.05)
	# trick: if we press right enough times we will always end up in the same place
    key(right)
	repeat(7) 
	key(tab)
	repeat(4)
	key(enter)
	#we now should be in the manage styles dialog
	#press import/export
	key(alt-x) 
	#close down the template file that comes up by default
	key(alt-e) 
	#open up the dialogue to get admin different file
	sleep(0.05)
	key(alt-e)
	#tab to get to the file type selector
	key(tab) 
	#select Microsoft Word files
	key(alt-down)
	key(up)
	repeat(10)
	key(down)
	key(enter)

finish export styles:
	#we have now chosen a file to export to enter back into the export dialog
	#tab our way to the list of styles
	key(tab)
	repeat(2)
	#select all of the styles - let's hope there is not more than this many
	key(shift-down)
	repeat(999)
	#press copy button
	key(alt-c)
	#yes to all warning messages
	key(alt-a)
	# Press tab five times to get the close button
	key(tab)
	repeat(4)
	#let's do this!
	key(enter)
	#finally close the styles pane
	key(alt-h)
	key(f)
	key(y)

#special symbols
insert checkmark:
	insert("2713")
	key(alt-x)
insert ex mark:
	insert("2715")
	key(alt-x)
insert alpha:
	insert("03b1")
	key(alt-x)
insert beta:
	insert("03b2")
	key(alt-x)
insert gamma:
	insert("03b3")
	key(alt-x)
insert delta:
	insert("03b4")
	key(alt-x)
insert theta:
	insert("03b8")
	key(alt-x)
insert lambda:
	insert("03bb")
	key(alt-x)
insert mu:
	insert("03bc")
	key(alt-x)
insert sigma:
	insert("03c3")
	key(alt-x)


# hyperlinks
(insert|add|create) hyperlink:
	key(alt-n)
	key(i)
	key(i)
remove hyperlink:
	key(alt-n)
	key(i)
	key(i)
	key(alt-r)
copy hyperlink:
	key(alt-n)
	key(i)
	key(i)
	sleep(0.1)
	key(ctrl-c)
	key(esc:3)
(apply|paste) hyperlink:
	key(alt-n)
	key(i)
	key(i)
	sleep(0.1)
	key(ctrl-v)
	sleep(0.1)
	key(enter)

	