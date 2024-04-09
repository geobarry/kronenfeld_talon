# TEMPLATE FROM COMMUNITY
# navigate [{user.arrow_key}] [{user.navigation_action}] [{user.navigation_target_name}] [{user.before_or_after}] [<user.ordinals>] <user.navigation_target>:


# MY COMMANDS - THESE SHOULD BE MOVED TO MY OWN FOLDER
select [<user.ordinals>] next <user.navigation_target>:
	user.navigation("SELECT","DOWN","DEFAULT","DEFAULT",navigation_target,ordinals or 1)
select [<user.ordinals>] previous <user.navigation_target>:
	user.navigation("SELECT","UP","DEFAULT","default",navigation_target,ordinals or 1)

extend {user.before_or_after} [<user.ordinals>] next <user.navigation_target>:
	user.navigation("EXTEND","DOWN","DEFAULT",before_or_after,navigation_target,ordinals or 1)
extend {user.before_or_after} [<user.ordinals>] previous <user.navigation_target>:
	user.navigation("EXTEND","UP","DEFAULT",before_or_after,navigation_target,ordinals or 1)

go {user.before_or_after} [<user.ordinals>] next <user.navigation_target>:
	user.navigation("GO","DOWN","DEFAULT",before_or_after,navigation_target,ordinals or 1)
go {user.before_or_after} [<user.ordinals>] previous <user.navigation_target>:
	user.navigation("GO","UP","DEFAULT",before_or_after,navigation_target,ordinals or 1)

phones [<user.ordinals>] previous <user.navigation_target>:
	user.navigation("SELECT","UP","DEFAULT","default",navigation_target,ordinals or 1)
	sleep(3)
	user.homophones_show_auto()

phones [<user.ordinals>] next <user.word>:
	user.navigation("SELECT","DOWN","DEFAULT","default",navigation_target,ordinals or 1)
	sleep(3)
	user.homophones_show_auto()
