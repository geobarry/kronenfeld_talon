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
convert to code: key(y)
convert to markdown: key(m)
convert to heading [one]: key(1)
convert to heading two: key(2)
convert to heading three: key(3)
select up: key(shift-up)
select down: key(shift-down)
insert [cell] [above]: key(a)
insert [cell] below: key(b)
cut cells: key(x)
copy cells: key(c)
paste [cells] [above]: key(shift-v)
paste [cells] below: key(v)
delete cells: key(d)
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
line break:
	insert("<br>")
insert code block:
	user.insert_between("<p style='color:#ee7;font-weight:bold;background-color:#225;font-family:Courier New,monospace;padding: 0.2em'>","</p>")
begin code block:
	insert("<p style='color:#ee7;font-weight:bold;background-color:#225;font-family:Courier New,monospace;padding: 0.2em'>")
end code block:
	insert("</p>")
insert code style:
	user.insert_between("<a style='color:#ee7;font-weight:bold;background-color:#225;font-family:Courier New,monospace;padding: 0.2em'>","</a>")
begin code style:
	insert("<a style='color:#ee7;font-weight:bold;background-color:#225;font-family:Courier New,monospace;padding: 0.2em'>")
end code style:
	insert("</a>")
angle brackets:
	user.insert_between("&lt;","&gt;")