app: windows_terminal
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