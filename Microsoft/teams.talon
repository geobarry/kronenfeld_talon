tag: user.teams
#app.exe: ms-teams.exe
# assumes talon is awake, teams is muted

-
unmute:
	speech.disable()	
	key(ctrl-shift-m)

test teams tag: print("Teams tag is active")