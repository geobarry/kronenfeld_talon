^access {user.dynamic_children}$:
    user.focus_element_by_name(dynamic_children)
copy accessible:
	user.copy_accessible_elements_to_clipboard()
	
^click {user.dynamic_children}$:
	user.click_element_by_name(dynamic_children)
^move [to] {user.dynamic_children}$:
	user.move_to_element(dynamic_children)
^copy focused element information$:
	user.copy_focused_element_to_clipboard()
^copy enabled element information$:
	user.copy_enabled_element_to_clipboard()
^copy clickable element information$:
	user.copy_clickable_element_to_clipboard()
^copy keyboard element information$:
	user.copy_keyboard_element_to_clipboard()
^copy all element information$:
	user.test_copy_all()