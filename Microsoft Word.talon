app: Microsoft Word
-
sub <user.letter>:
	insert(" ")
	edit.left()
	key(alt-h)
	key(5)
	insert("{user.letter}")
	key(alt-h)
	key(5)
	edit.right()
	
sub <number>:
	insert(" ")
	edit.left()
	key(alt-h)
	key(5)
	insert("{number}")
	key(alt-h)
	key(5)
	edit.right()
	
apply style:
	key(alt-h)
	key(z)
	key(1)
	key(y)
	key(1)
	
apply heading <number>:
	key(alt-h)
	key(z)
	key(1)
	key(y)
	key(1)
	insert("Heading ")
	insert("{number}")
	key(enter)

apply normal:
	key(alt-h)
	key(z)
	key(1)
	key(y)
	key(1)
	insert("normal")
	key(enter)
	
style match selection:
	key(alt-h)
	key(f)
	key(y)
	key(right)
	key(alt-down)
	key(enter)
	key(alt-h)
	key(f)
	key(y)

figure <number> here:
	insert("<figure ")
	insert("{number}")
	insert(" approximately here>")

table <number> here:
	insert("<table ")
	insert("{number}")
	insert(" approximately here>")
	
apply bullets:
	key(alt-h)
	key(u)
	key(right)

save as:
	key(alt-f)
	sleep(0.05)
	key(a)