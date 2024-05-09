os: windows
and app.name: Windows Explorer
os: windows
and app.exe: explorer.exe

-
open with notepad: user.slow_key_press("menu w n enter",0.5)

# override default because default doesn't work
go <user.system_path>:
	key(alt-d)
	sleep(0.2)
	insert(system_path)
	sleep(0.2)
	key(enter)
	# get rid of annoying dropdown suggestions that don't disappear on their own
	sleep(0.5)
	key(alt-d)
	sleep(0.5)
	key(esc tab:2)
	sleep(0.5)
	key(tab:5)
	# returned to file area
	user.file_explorer_tab_to_files()

tab to files: user.file_explorer_tab_to_files()

copy full path: user.file_explorer_copy_full_path()
copy folder: user.file_explorer_copy_folder()

go to <user.text>:
	insert(text)

# sorting
extract: user.slow_key_press("menu t 2",2.5)
sort by {user.explorer_heading}: user.file_explorer_sort_by(explorer_heading)
address bar: key(alt-d)

compress video [file]: user.compress_video_file()
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
	sleep(0.5)
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

replace with underscores: user.replace_with_underscores()

# alternate views
large icons: key(ctrl-shift-1)
medium icons: key(ctrl-shift-2)
small icons: key(ctrl-shift-3)
list view: key(ctrl-shift-4)
detailed view: key(ctrl-shift-6)
distraction free [view]: key(ctrl-shift-5)
# very specific idiosyncratic commands
process desire to learn downloads:
	user.process_desire_to_learn_downloads()
	