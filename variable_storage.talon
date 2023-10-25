save variable <user.text>:
	user.save_variable(text, edit.selected_text())
remove variable <user.text>:
	user.remove_variable(text)
variable {user.variable_list} equals <number>:
	insert(variable_list)
	insert(" = ")
	insert(number)

# person list
save person <user.text>:
	user.save_person(text, edit.selected_text())
remove person <user.text>:
	user.remove_person(text)
person name {user.person_list}:
	insert(person_list)
	insert(" ")
greet {user.person_list}:
	insert("Hi ")
	insert(person_list)
	insert(",")
	key(enter)
