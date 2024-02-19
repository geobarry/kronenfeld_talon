# variable list
(create|save) variable <user.text>:
	user.save_variable(text, edit.selected_text())
remove variable {user.variable_list}:
	user.remove_variable(variable_list)

# module list
(create|save) module <user.text>:
	user.save_module(text, edit.selected_text())
remove module {user.module_list}:
	user.remove_module(module_list)

# function list
(create|save) function <user.text>:
	user.save_function(text, edit.selected_text())
remove function {user.function_list}:
	user.remove_function(function_list)

# keyword list
(create|save) keyword <user.text>:
	user.save_keyword(text, edit.selected_text())
remove keyword {user.keyword_list}:
	user.remove_keyword(keyword_list)

# app list
(create|save) app <user.text>:
	user.save_app(text, edit.selected_text())
remove app {user.app_list}:
	user.remove_app(app_list)
launch app {user.app_list}: 
	key(super)
	sleep(1.0)
	insert("{app_list}")
	sleep(1.0)
	key(enter)

# person list
(create|save) person <user.text>:
	user.save_person(text, edit.selected_text())
remove person {user.person_list}:
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