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
	insert("Hi {person_list},")
	key(enter:2)
greet {user.person_list} and {user.person_list}:
	insert("Hi {person_list_1} and {person_list_2},")
	key(enter:2)
(formal|formally) greet {user.person_list}:
	insert("Dear {person_list},")
	key(enter:2)
{user.person_list} possessive:
	insert("{person_list}'s ")
{user.person_list} and others possessive:
	insert("{person_list} et al's ")
{user.person_list} and others:
	insert("{person_list} et al. ")
doctor {user.person_list}:
	insert("Dr. {person_list}")