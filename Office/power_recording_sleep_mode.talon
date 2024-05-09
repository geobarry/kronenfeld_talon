mode: sleep
and tag: user.power_recording
-
stop recording: 
	speech.enable()
	key(s)	
next slide$:
	speech.enable()
	key(s)
next (point|item|bullet|animation|line|line of code)$:
	speech.enable()
	key(space)
	speech.disable()
	
	