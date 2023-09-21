app.exe: cmd.exe
app.exe: WindowsTerminal.exe
app.exe: conhost.exe

- 
show cheat sheet:
	insert("cd %appdata%/Talon/user/cheat sheet")
	key("enter")
	insert("python -m http.server 8080")
	key("enter")

start server:
	insert("python -m http.server 8080")
	
start server <number>:
	insert("python -m http.server {number}")
	
start node server:
	insert("npm start")
	key("enter")
	
conda list environments:
	insert("conda env list")
	key(enter)
conda install:
	insert("conda install ")
conda activate:
	insert('activate ')
conda create:
	insert('conda create ')
	
open spider app:
	insert('spyder')

# ffmpeg
convert clipboard movie:
	insert('ffmpeg -i ')
	edit.paste()
	insert(' -c:v libx264 -c:a aac ')