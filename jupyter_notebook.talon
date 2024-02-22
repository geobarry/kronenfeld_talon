tag: user.jupyter_notebook
-
edit mode:
	key(enter)
command mode:
	key(esc)
open command palette: key(ctrl-shift-f)
(run|execute) (code|cell):
	key(shift-enter)
(run|execute) in place:
	key(shift-enter)
	sleep(0.1)
	key(up)
run selected: key(ctrl-enter)
run and insert: key(alt-enter)
collapse: key(left:2)
collapse all: key(ctrl-shift-left)
expand: key(right)
select section: key(shift-right)
expand all: key(ctrl-shift-right)
insert heading [cell] [above]: key(shift-a)
insert heading [cell] below: key(shift-b)
convert to code: key(esc y)
convert to markdown: key(esc m)
convert to heading [one]: key(1)
convert to heading two: key(2)
convert to heading three: key(3)
select up: key(shift-up)
select down: key(shift-down)
insert [cell] [above]: key(a)
insert [cell] below: key(b)
(delete|cut) cells: key(esc x)
copy cells: key(c)
paste [cells] [above]: key(shift-v)
paste [cells] below: key(v)
#delete cells: key(d)
undo delete cells: key(z)
merge cells: key(shift-m)
save notebook: key(s)
[toggle] line numbers: key(l)
toggle all line numbers: key(shift-l)
toggle output: key(o)
toggle scrolling: key(shift-o)
(help|show [keyboard] shortcuts): key(h)
interrupt [kernel]: key(is)
scroll up: key(shift-space)
scroll down: key(space)
(complete code|code completion): key(tab)
show tooltip: key(shift-tab)
indent: key(ctrl-])
(unindent|dedent): key(ctrl-[)
[toggle] comment: key(ctrl-/)
delete line: key(ctrl-d)
go to cell start: key(ctrl-up)
go to sell end: key(ctrl-down)
split cell: key(ctrl-shift-minus)

inline command:
	user.insert_between("**<a style='color:#b10;font-family:Courier New,monospace'>","</a>**")
begin command style:
	insert("**<a style='color:#b10;font-family:Courier New,monospace'>")
end command style:
	insert("</a>**")
[insert] line break:
	insert("<br>")
insert code block:
	user.insert_between("<p style='color:#ee7;font-weight:bold;background-color:#225;font-family:Courier New,monospace;padding: 0.2em'>","</p>")
begin code block:
	insert("<p style='color:#ee7;font-weight:bold;background-color:#225;font-family:Courier New,monospace;padding: 0.2em'>")
end code block:
	insert("</p>")
insert code style:
	user.insert_between("<a style='color:#24b;font-weight:bold;font-family:Courier New,monospace;padding: 0.2em'>","</a>")
begin code style:
	insert("<a style='color:#24b;font-weight:bold;font-family:Courier New,monospace;padding: 0.2em'>")
end code style:
	insert("</a>")
begin comment style:
	insert("<a style='color:#b27;font-style:italic;font-family:Cursive,Brush Script MT;padding: 0.2em'>")
end comment style:
	insert("</a>")

(give feedback|insert comment cell) [below]:
	key(b m enter)
	insert("<a style='color:#b27;font-style:italic;font-family:Cursive,Brush Script MT;padding: 0.2em'>")
	sleep(0.3)
	key(enter:2)
	insert("</a>")
	sleep(0.2)
	key(up)
(give good feedback|insert good comment):
	key(b m enter)
	insert("<a style='color:#b27;font-style:italic;font-family:Cursive,Brush Script MT;padding: 0.2em'>")
	sleep(0.3)
	key(enter:2)
	insert("</a>")
	sleep(0.2)
	key(up)
	insert("good")
	sleep(0.2)
	key(shift-enter)
	
# Hypertext Markup Language	
# This really should be broken out into a different talon file
begin [unordered] list: insert("<ul>")
end [unordered] list: insert("</ul>")
[insert] list item: insert("<li>")
angle brackets: user.insert_between("&lt;","&gt;")
character space: insert("&nbsp;")