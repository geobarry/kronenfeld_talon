tag: user.power_recording
-
# Is there a way to deactivate commands???
exit recording:
	key(esc)
	user.deactivate_power_recording()

toggle teleprompter:
	key(t)
toggle presenter view:
	key(ctrl-n)
scroll down:
	key(ctrl-down)
clear recording:
	key(ctrl-d)
scroll up:
	key(ctrl-up)
start recording:
	speech.disable()
	key(r)
okay moving on:
	speech.enable()
stop recording:
	key(s)
retake recording:
	speech.disable()
	key(ctrl-r)
	
