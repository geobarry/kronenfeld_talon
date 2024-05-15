tag: user.power_screen_recording
-
select area: key(super-shift-a)
select full screen: user.power_select_full_screen()
start recording:
	user.click_spot("record")
	speech.disable()
#	key(super-shift-r)
(next slide$|stop recording): 
	speech.enable()
	key(super-shift-q)	
	user.deactivate_power_screen_recording()
