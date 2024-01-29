tag: zoom
and mode: sleep
# assumes zoom is unmuted
-
noise(pop):
	# user function to catch two pops in a row
	# (because I often make a single popping noise by accident)
	user.mute_zoom_on_double_pop()
