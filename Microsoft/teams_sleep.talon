#app.exe: ms-teams.exe
tag: user.teams
and mode: sleep
# assumes teams is unmuted
-
noise(pop):
	# user function to catch two pops in a row
	# (because I often make a single popping noise by accident)
	user.mute_teams_on_double_pop()
	print("Popping noise detected in teams")