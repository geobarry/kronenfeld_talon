# variable list
(create|save) variable <user.text>:
	user.save_variable(text, edit.selected_text())
remove variable <user.text>:
	user.remove_variable(text)

# module list
(create|save) module <user.text>:
	user.save_module(text, edit.selected_text())
remove module <user.text>:
	user.remove_module(text)

# person list
(create|save) person <user.text>:
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
	key(enter)
greet {user.person_list} and {user.person_list}:
	insert("Hi ")
	insert("{person_list_1} and {person_list_2},")
	key(enter)
	key(enter)
{user.person_list} no:
	insert("{person_list}'s ")
{user.person_list} and others know:
	insert("{person_list} et al's ")
