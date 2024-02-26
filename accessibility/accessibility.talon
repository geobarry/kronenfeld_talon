^access {user.dynamic_children}$:
    user.focus_element_by_name(dynamic_children)
copy accessible:
	user.copy_accessible_elements_to_clipboard()
	
^click {user.dynamic_children}$:
	user.click_element_by_name(dynamic_children)
^move [to] {user.dynamic_children}$:
	user.move_to_element(dynamic_children)
^copy element information$:
	user.copy_focused_element_to_clipboard()