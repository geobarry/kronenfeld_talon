os: windows
and app.name: Microsoft Excel
os: windows
and app.exe: EXCEL.EXE
-
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
auto fit column:
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
auto fit row:
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
freeze panes:
	key(alt-w)
	key(f)
	key(f)
	