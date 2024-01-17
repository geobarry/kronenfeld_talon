tag: user.fast_spots
-
user.screen_spots_slow_move_enabled = 1
user.setting_slow_move_distance = 25
click <user.text>: 
	user.move_to_spot(user.text)
	sleep(0.5)
	mouse_click(0)
