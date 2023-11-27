os: windows
and app.name: Microsoft Excel
os: windows
and app.exe: EXCEL.EXE
-
tag(): user.excel_powerpoint_shared
# common office shortcuts
save as:
	key(alt-f)
	sleep(0.05)
	key(a)

# worksheets
next (tab|sheet|worksheet):
	key(ctrl-pagedown)
previous (tab|sheet|worksheet):
	key(ctrl-pageup)
new (tab|sheet|worksheet):
	key(alt-h)
	key(i)
	key(s)
delete (tab|sheet|worksheet):
	key(alt-h)
	key(d)
	key(s)
rename (tab|sheet|worksheet):
	key(alt-h)
	key(o)
	key(r)
	
# columns
insert column:
	key(alt-h)
	key(i)
	key(c)
delete column:
	key(alt-h)
	key(d)
	key(c)
column width:
	key(alt-h)
	key(o)
	key(w)
auto fit (column|width|column width):
	key(alt-h)
	key(o)
	key(i)
	
# rows
insert row:
	key(alt-h)
	key(i)
	key(r)
delete row:
	key(alt-h)
	key(d)
	key(r)
row height:
	key(alt-h)
	key(o)
	key(h)
auto fit (row|height|row height):
	key(alt-h)
	key(o)
	key(a)	
	
	
# [ribbon|menu] headings
file [ribbon|menu]:
	key(alt-f)
home [ribbon|menu]:
	key(alt-h)
insert [ribbon|menu]:
	key(alt-n)
page layout [ribbon|menu]:
	key(alt-p)
formula [ribbon|menu]:
	key(alt-m)
data [ribbon|menu]:
	key(alt-a)
review [ribbon|menu]:
	key(alt-r)
(view|you) [ribbon|menu]:
	key(alt-w)
automate [ribbon|menu]:
	key(alt-u)
help [ribbon|menu]:
	key(alt-y)
	key(1)
excel toolbox [ribbon|menu]:
	key(alt-y)
	key(2)

# home menu
paste values:
	key(alt-e)
	key(s)
	key(v)
	key(enter)
font color: 
	key(alt-h)
	key(f)
	key(c)
highlight cell:
	key(alt-h)
	key(h)
	sleep(0.1)
	key(up:4)
	key(left:6)
(apply|toggle) word wrap:
	key(alt-h)
	key(w)
format number <number> decimal places:
	key(alt-h)
	key(f)
	key(m)
	key(tab)
	key(up:12)
	key(down)
	key(alt-d)
	insert(number)
	key(enter)

# data menu
sort:
	key(alt-a)
	key(s)
	key(s)
	
# view menu
freeze top row:
	key(alt-w)
	key(f)
	key(r)
[toggle] freeze panes:
	key(alt-w)
	key(f)
	key(f)
#view ribbon shortcuts
zoom <number> [percent]:
	key(alt-w)
	sleep(0.1)
	key(q)
	sleep(0.1)
	key(c)
	sleep(0.1)
	insert(number)
	key(enter)


##formulas
(formula|equation) concatenate:
	insert("concat(")
(formula|equation) (max|maximum):
	insert("max(")
(formula|equation) minimum:
	insert("min(")
(formula|equation) sum:
	insert("sum(")
(formula|equation) some product:
	insert("sumproduct(")
(formula|equation) if:
	insert("if(")
(formula|equation) text:
	insert("text(")
(formula|equation) text join:
	insert("textjoin(")
(formula|equation) character:
	insert("char(")
(formula|equation) square root:
	insert("sqrt(")

column <user.letter>:
	insert("{letter}:{letter}")
