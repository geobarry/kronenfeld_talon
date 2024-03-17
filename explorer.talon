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
	sleep(0.2)
	insert(system_path)
	sleep(0.2)
	key(enter)
#	sleep(1.5)
#	key(escape)

#	user.file_manager_open_directory(system_path)

go to <user.text>:
	insert(text)

# sorting
extract: user.slow_key_press("menu t 2",1.5)
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

compress video [file]:
	user.compress_video_file()
open file locator:
	# grab path to current folder
	key(alt-d)
	sleep(0.5)
	edit.copy()
	# launch file locator
	key(super)
	sleep(1.0)
	insert("filelocator")
	sleep(1.0)
	key(enter)
	sleep(1.5)
	# remove default file name and enter the folder path
	key(del)
	key(tab:2)
	sleep(1)
	edit.paste()
	sleep(1)
	key(shift-tab)

open jupyter [notebook]:
	# grab path to current folder
	key(alt-d)
	sleep(0.5)
	edit.copy()
	# open the python command prompt
	key(super)
	sleep(0.5)
	insert("python command prompt")
	sleep(0.5)
	key(enter)
	sleep(2.5)
	# change directories and open jupyter notebook
	insert("cd ")
	sleep(0.5)
	edit.paste()
	sleep(0.5)
	key(enter)
	insert("jupyter notebook")
	key(enter)
	
new file:
	key(alt-up)
	sleep(0.2)
	key(enter)
	sleep(1.0)
	key(menu)
	sleep(0.2)
	key(w 1)
	sleep(0.2)
	key(up:3)
new folder: key(ctrl-shift-n)
zip selected:
	key(menu)
	sleep(0.5)
	key(z)

large icons: key(ctrl-shift-1)
medium icons: key(ctrl-shift-2)
small icons: key(ctrl-shift-3)
list view: key(ctrl-shift-4)
detailed view: key(ctrl-shift-6)
distraction free [view]: key(ctrl-shift-5)
# very specific idiosyncratic commands
process desire to learn downloads:
	user.process_desire_to_learn_downloads()
	