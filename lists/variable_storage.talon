#use this to save a list from storage into a CSV:
# 	user.write_list("keywords.talon-list","keyword_list")

switch order: user.switch_order()

create person <user.text>:
	user.save_to_list("persons.talon-list",text,edit.selected_text())
create variable <user.text>:
	user.save_to_list("variables.talon-list",text,edit.selected_text())
create module <user.text>:
	user.save_to_list("modules.talon-list",text,edit.selected_text())
create app <user.text>:
	user.save_to_list("apps.talon-list",text,edit.selected_text())
create function <user.text>:
	user.save_to_list("functions.talon-list",text,edit.selected_text())
create keyword <user.text>:
	user.save_to_list("keywords.talon-list",text,edit.selected_text())

customize {user.named_list}: user.customize_named_list(named_list)

launch app {user.app_list}: 
	key(super)
	sleep(1.0)
	insert("{app_list}")
	sleep(1.0)
	key(enter)

# person list
person name {user.person_list}: insert("{person_list} ")
given name {user.person_list}: insert("{user.insert_nth_word(person_list,0,' ')} ")
family name {user.person_list}: insert("{user.insert_nth_word(person_list,1,' ')} ")
greet {user.person_list}: insert("Hi {user.insert_nth_word(person_list,0,' ')},\n\n")

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