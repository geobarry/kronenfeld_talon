browser.url: /online/
-
new file from computer: user.D2L_add_new_file_from_computer()
score <user.real_number>: user.D2L_assign_score(real_number)
expand feedback:
	user.key_to_name_and_class("tab","Expand.*feedback.*","d2l-hpg-opener")
	key("enter tab:2")
collapse feedback:
	user.key_to_name_and_class("shift-tab","Collapse.*feedback.*","d2l-hpg-opener")
go to feedback: user.key_to_name_and_class("Feedback","mce-content-body d2l-html-block-rendered")
add feedback:
	user.key_to_name_and_class("tab","Options","d2l-dropdown-opener")
	key(enter)
	user.key_to_name_and_class("down","Add Feedback")
	key(enter esc)
	user.key_to_name_and_class("tab","Edit Overall Feedback")
	user.click_focused()
(save and continue|continue next): 
	user.key_to_name_and_class("tab","Save and Continue","d2l-button")
	key("enter")
just save: 
	user.key_to_name_and_class("tab","Save","d2l-button")
	key("enter")
go back to questions:
	user.key_to_name_and_class("tab","Go Back to Questions","d2l-button")
	key("enter")
show <user.text> actions:
	user.key_to_name_and_class("tab","Actions.*{text}.*")
	key(enter)