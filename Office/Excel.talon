os: windows
and app.name: Microsoft Excel
os: windows
and app.exe: EXCEL.EXE
-
tag(): user.excel_powerpoint_shared
# common office shortcuts
save as: key(alt f a)

# worksheets
next (tab|sheet|worksheet): key(ctrl-pagedown)
previous (tab|sheet|worksheet): key(ctrl-pageup)
(insert|new) (tab|sheet|worksheet): key(alt-h i s)
delete (tab|sheet|worksheet): key(alt-h d s)
rename (tab|sheet|worksheet): key(alt-h o r)
move (tab|sheet|worksheet): key(alt-h o m)
	
# columns
insert column: key(alt-h i c)
delete column: key(alt-h d c)
column width: key(alt-h o w)
auto fit (column|width|column width): key(alt-h o i)
select column: key(ctrl-space)
hide column: key(ctrl-0)
select column <user.letter>:
	key(alt-f3)
	insert("{letter}1")
	key(enter ctrl-space)
paste into column <user.letter>:
	key(alt-f3)
	insert("{letter}1")
	key(enter ctrl-space ctrl-v)
	
# rows
insert row: key(alt-h i r)
delete row: key(alt-h d r)
row height: key(alt-h o h)
auto fit (row|height|row height): key(alt-h o a)
select row: key(shift-space)
hide row: key(ctrl-9)
select row <number>:
	key(alt-f3)
	insert("a{number}")
	key(enter shift-space)
paste into row <number>:
	key(ctrl-x alt-f3)
	insert("a{number}")
	key(enter shift-space ctrl-v)


# cells
go to cell: key(alt-f3)
go to cell <user.letter> <number>:  
	key(alt-f3)
	insert("{user.letter}{number}")
	key(enter)
go to {user.person_list}: user.go_excel_row_by_person(person_list,0.2)
score {user.person_list} <user.real_number>:
	user.go_excel_row_by_person(person_list,0.3)
	sleep(0.2)
	insert("{real_number}")
	key(enter up)

# [ribbon|menu] headings
file [ribbon|menu]: key(alt-f)
home [ribbon|menu]: key(alt-h)
insert [ribbon|menu]: 	key(alt-n)
page layout [ribbon|menu]: 	key(alt-p)
formula [ribbon|menu]: 	key(alt-m)
data [ribbon|menu]: 	key(alt-a)
review [ribbon|menu]: 	key(alt-r)
(view|you) [ribbon|menu]: 	key(alt-w)
automate [ribbon|menu]: 	key(alt-u)
help [ribbon|menu]: 	key(alt y 1)
excel toolbox [ribbon|menu]: key(alt-y 2)
chart design menu: key(alt j c)
chart format menu: key(alt j a)
	
# home menu
paste special: key(alt-h v s)
paste values: key(alt-e s v enter)
paste transposed: key(alt-h v s e enter)
paste transposed values: key(alt-h v s e v enter)
paste external: key(alt-h v m)
paste single line:
	user.make_clipboard_one_line(", ")
	key(ctrl-v)
font color:  key(alt-h f c)
highlight cell:
	key(alt-h h)
	sleep(0.1)
	key(up:4 left:6)
[(apply|toggle)] word wrap: key(alt-h w) 
format number <number> decimal places: 
	key(alt-h f m tab up:12 down alt-d)
	insert(number)
	key(enter)

# data menu
sort: key(alt-a s:2)
	
# view menu
freeze top row: key(alt w f r)
[toggle] freeze panes: key(alt w f:2)
zoom <number> [percent]:
	key(alt-w q c)
	insert(number)
	key(enter)
	
# chart shortcuts
select (object|chart|graph):
	key(alt w k)
	sleep(1)
	key(tab)
	sleep(0.1)
	key(tab)
	sleep(0.1)
	key(tab)
	key(down:2)
close navigation [pane]:
	key(alt-w)
	key(k)
	sleep(0.08)
	key(ctrl-space)
	sleep(0.08)
	key(c)
select only (object|chart|graph):
	key(alt-w)
	key(k)
	sleep(1)
	key(tab)
	sleep(0.1)
	key(tab)
	sleep(0.1)
	key(tab)
	key(down:2)
	key(enter)
	sleep(0.5)
	key(alt-w)
	key(k)
	sleep(0.5)
	key(ctrl-space)
	key(c)

select [chart] item: key(alt j a e alt-down)
format selected (element|item): key(menu up enter)
add [chart] (element|item): key(alt j c a)
add horizontal axis title: key(alt j c a a h)
add vertical axis title: key(alt j c a a v)
add [chart] title: key(alt j c a c a)
format [chart] title:
	key(alt j a e alt-down down)
	sleep(0.2)
	key(enter)

exit (pane|panel): key(ctrl-space c)

##formulas
(formula|equation) concatenate: insert("concat(")
(formula|equation) (max|maximum): insert("max(")
(formula|equation) minimum: insert("min(")
(formula|equation) sum: insert("sum(")
(formula|equation) average: insert("average(")
(formula|equation) some product:	insert("sumproduct(")
(formula|equation) if: insert("if(")
(formula|equation) text: insert("text(")
(formula|equation) text join: insert("textjoin(")
(formula|equation) character: insert("char(")
(formula|equation) square root: insert("sqrt(")
(formula|equation) normal distribution: insert("norm.dist(")
(formula|equation) count if: insert("countif(")

average <user.letter>: insert("=average({letter}:{letter})")
minimum <user.letter>: insert("=min({letter}:{letter})")
maximum <user.letter>: insert("=max({letter}:{letter})")

[(formula|equation)] line break: insert("char(10)")
column <user.letter>: insert("{letter}:{letter}")

