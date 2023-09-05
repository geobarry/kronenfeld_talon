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
	key(right)
	# trick: if we press right enough times we will always end up in the same place
	repeat(7) 
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


# common operations	
copy style:
	key(ctrl-shift-c)
paste style:
	key(ctrl-shift-v)

view text width:
	key(alt-w)
	sleep(0.15)
	key(q)
	key(alt-t)
	key(enter)	
# center on screen by toggling between webview and print view
# strangely this doesn't work when we put the two key sequences together
view web:
	key(alt-w)
	sleep(0.15)
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