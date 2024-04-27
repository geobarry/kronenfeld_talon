browser.url: /populationpyramid/
# https://www.populationpyramid.net/world/2023/
-
<user.letter> countries$: 
	user.key_to_elem_by_val("tab","{letter}","name",999)
	sleep(0.3)
	key(enter)
country <user.text>$: 
	user.key_to_elem_by_val("tab",text,"name",99)
	sleep(0.3)
	key(enter)
download pyramid$:
	user.key_to_elem_by_val("shift-tab","Download","name",99)
	sleep(0.3)
	key(enter)