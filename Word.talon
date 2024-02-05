app: Microsoft Word

-
toggle ribbon:
	key(ctrl-f1)
  
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

close panel: key(f6 ctrl-space c)
exit panel:	key(ctrl-space c)
	
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

#home menu ribbon shortcuts
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
remove (paragraph|line) spacing:
	key(alt-h)
	sleep(0.05)
	key(p)
	key(g)
	key(alt-f)
	insert("0")
	key(enter)
apply bold:
	key(alt-h)
	key(1)
apply (italic|italics):
	key(alt-h)
	key(2)
apply underline:
	key(alt-h)
	key(3)
apply strike through:
	key(alt-h)
	key(4)
apply subscript:
	key(alt-h)
	key(f)
	key(n)
	key(alt-b)
	key(enter)
apply superscript:
	key(alt-h)
	key(f)
	key(n)
	key(alt-p)
	key(enter)
list indent:
	key(alt)
	sleep(0.2)
	key(h a i)
list dedent:
	key(alt)
	sleep(0.2)
	key(h a o)
align left:
	key(alt-h)
	key(a)
	key(l)
align center:
	key(alt-h)
	key(a)
	key(c)
align right:
	key(alt-h)
	key(a)
	key(r)
justify top:
	key(alt-h)
	

	
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

# layout menu shortcuts
insert page break:
	key(alt)
	sleep(0.2)
	key(p b p)
insert column break:
	key(alt)
	sleep(0.2)
	key(p b c)

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
	insert("{number}")
	insert("%")
	key(enter)
	
# menu review
delete all comments:
	key(alt)
	sleep(0.2)
	key(r d o)
accept all changes [and stop tracking]:
	key(alt)
	sleep(0.2)
	key(r a 2 s)
# menu table design
table border none:
	key(alt)
	sleep(0.2)
	key(j)
	key(t)
	key(b)
	key(n)
table border top:
	key(alt)
	sleep(0.2)
	key(j)
	key(t)
	key(b)
	key(p)
table border bottom:
	key(alt)
	sleep(0.2)
	key(j)
	key(t)
	key(b)
	key(b)
table border left:
	key(alt)
	sleep(0.2)
	key(j)
	key(t)
	key(b)
	key(l)
table border right:
	key(alt)
	sleep(0.2)
	key(j)
	key(t)
	key(b)
	key(r)
table border all:
	key(alt)
	sleep(0.2)
	key(j)
	key(t)
	key(b)
	key(a)
	
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
insert column [left]:
	key(alt)
	sleep(0.2)
	key(j l l)
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
delete table:
	key(alt)
	key(j)
	sleep(0.2)
	key(l)
	key(d)
	key(t)
(align|justify) top left:
	key(alt)
	sleep(0.2)
	key(j)
	key(l)
	key(t)
	key(l)
(align|justify) top center:
	key(alt)
	sleep(0.2)
	key(j)
	key(l)
	key(t)
	key(c)
(align|justify) top right:
	key(alt)
	sleep(0.2)
	key(j)
	key(l)
	key(t)
	key(r)
(align|justify) center left:
	key(alt)
	sleep(0.2)
	key(j)
	key(l)
	key(c)
	key(l)
(align center middle|justify center [middle]):
	key(alt)
	sleep(0.2)
	key(j)
	key(l)
	key(c)
	key(c)
(align|justify) center right:
	key(alt)
	sleep(0.2)
	key(j)
	key(l)
	key(c)
	key(r)
(align|justify) bottom left:
	key(alt)
	sleep(0.2)
	key(j)
	key(l)
	key(b)
	key(l)
(align|justify) bottom center:
	key(alt)
	sleep(0.2)
	key(j)
	key(l)
	key(b)
	key(c)
(align|justify) bottom right:
	key(alt)
	sleep(0.2)
	key(j)
	key(l)
	key(b)
	key(r)

# picture format menu
toggle [lock] picture aspect [ratio]:
	key(alt)
	sleep(0.2)
	key(j)
	key(p)
	key(s)
	key(z)
	sleep(0.1)
	key(a)
	key(enter)
picture height:
	key(alt)
	sleep(0.2)
	key(j)
	key(p)
	key(h)
picture height <number>:
	key(alt)
	sleep(0.2)
	key(j)
	key(p)
	key(h)
	sleep(0.1)
	insert(number)
	key(enter)
	key(esc)
picture color options:
	key(alt)
	sleep(0.2)
	key(j p i c)
	
# equation menu 
insert equation:
	key(alt)
	sleep(0.2)
	key(n)
	key(e)
	key(i)
(equation|insert) script:
	key(alt)
	sleep(0.2)
	key(j)
	sleep(0.2)
	key(e)
	key(s)
(equation|insert) fraction:
	key(alt)
	sleep(0.2)
	key(j)
	key(e)
	key(f)
(equation|insert) accent:
	key(alt)
	sleep(0.2)
	key(j)
	key(e)
	key(a)
equation symbol:
	key(alt)
	sleep(0.2)
	key(j)
	key(e)
	key(q)
	
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
insert symbol:
	key(alt-n)
	key(u)
	key(m)
	sleep(0.2)
	key(alt-f)
	insert("symbol")
	key(enter)
	key(tab)
insert dot symbol: user.unicode_word("2022","Times New Roman")
insert (times|multiply|multiplication) symbol: user.unicode_word("00d7","Times New Roman")
insert checkmark: user.unicode_word("2713","Times New Roman")
insert ex mark:	user.unicode_word("2715","Times New Roman")
insert alpha: user.unicode_word("03b1","Times New Roman")
insert beta: user.unicode_word("03b2","Times New Roman")
insert gamma: user.unicode_word("03b3","Times New Roman")
insert delta: user.unicode_word("03b4","Times New Roman")
insert theta: user.unicode_word("03b8","Times New Roman")
insert lambda: user.unicode_word("03bb","Times New Roman")
insert mu: user.unicode_word("03bc","Times New Roman")
insert sigma: user.unicode_word("03c3","Times New Roman")
insert double arrow: user.unicode_word("00ab","Symbol")
insert left arrow: user.unicode_word("00ac","Symbol")
insert up arrow: user.unicode_word("00ad","Symbol")
insert right arrow: user.unicode_word("00ae","Symbol")
insert down arrow: user.unicode_word("00af","Symbol")
insert cursive el: user.unicode_word("2113","Times New Roman")
insert circled <user.letter>: user.circle_letter_word(letter)
insert cursive look: user.unicode_word("2113","times new roman")

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

	