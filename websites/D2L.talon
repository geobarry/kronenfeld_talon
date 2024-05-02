browser.url: /online/
-
new file from computer: user.D2L_add_new_file_from_computer()
score <user.real_number>: user.D2L_assign_score(real_number)
expand feedback:
	user.tab_to("Expand.*feedback.*","d2l-hpg-opener")
	key("enter tab:2")
collapse feedback:
	user.key_to("shift-tab","Collapse.*feedback.*","d2l-hpg-opener")
go to feedback: user.tab_to("Feedback","mce-content-body d2l-html-block-rendered")
add feedback:
	user.tab_to("Options","d2l-dropdown-opener")
	key(enter)
	user.key_to("down","Add Feedback")
	key(enter esc)
	user.tab_to("Edit Overall Feedback")
	user.click_focused()
(save and continue|continue next): 
	user.tab_to("Save and Continue","d2l-button")
	key("enter")
just save: 
	user.tab_to("Save","d2l-button")
	key("enter")
go back to questions:
	user.tab_to("Go Back to Questions","d2l-button")
	key("enter")
hunt [for] <user.text>:
	user.tab_to("{text}")
show <user.text> actions:
	user.tab_to("Actions.*{text}.*")
	key(enter)