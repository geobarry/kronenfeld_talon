^access {user.dynamic_children}$:
    user.focus_element_by_name(dynamic_children)
copy accessible:
	user.copy_accessible_elements_to_clipboard()
	
^click on {user.dynamic_children}$:
	user.click_element_by_name(dynamic_children)
^click word <user.word>$:
	user.click_element_by_name(word)

^click letter <user.letter>$:
	user.click_element_by_name(letter,1)

^{user.nav_key} to <user.text>$:
	key("{nav_key}")
	user.key_to(nav_key,"{text}.*","",20)
	
^move [to] {user.dynamic_children}$: user.move_to_element(dynamic_children)
^copy focused element information$: user.copy_focused_element_to_clipboard()
^copy focused element with children$: user.copy_focused_element_with_children(1)
^copy focused element with grandchildren$: user.copy_focused_element_with_children(2)
^copy focused element with great grandchildren$: user.copy_focused_element_with_children(3)
^copy focused element with <number> generations$: user.copy_focused_element_with_children(number)
^copy enabled element information$: user.copy_enabled_element_to_clipboard()
^copy clickable element information$: user.copy_clickable_element_to_clipboard()
^copy keyboard element information$: user.copy_keyboard_element_to_clipboard()
^copy all element information$: user.test_copy_all()
^copy mouse element information$: user.copy_mouse_elements_to_clipboard()
^copy selected element information$: user.copy_selected_elements_to_clipboard()
^copy tab element information$: user.copy_elements_accessible_by_key("tab",99)
^copy <user.special_key> element information$: user.copy_elements_accessible_by_key(special_key)
^copy <user.arrow_key> element information$: user.copy_elements_accessible_by_key(arrow_key)