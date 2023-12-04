os: windows
and app.name: Windows Explorer
os: windows
and app.exe: explorer.exe

-
open with notepad:
	key(menu)
	sleep(0.5)
	key(w)
	sleep(0.5)
	key(n)
	key(enter)

# override default because default doesn't work
go <user.system_path>:
	key(alt-d)
	sleep(0.5)
	insert(system_path)
	key(enter)
	key(escape)

#	user.file_manager_open_directory(system_path)

go to <user.text>:
	insert(text)

# sorting
sort:
	# get into the menu
	key(alt)
	# a sort menu is third from the right
	key(right:20)
	key(left:2)
	key(enter)
sort by name:
	# get into the menu
	key(alt)
	# sort menu is third from the right
	key(right:20)
	key(left:2)
	key(enter)
	# default is by name
	sleep(0.05)
	key(enter)
sort by date:
	# get into the menu
	key(alt)
	# sort menu is third from the right
	key(right:20)
	key(left:2)
	key(enter)
	# go down one to sort by date
	sleep(0.05)
	key(down)
	sleep(0.05)
	key(enter)
address bar:
	key(alt-d)