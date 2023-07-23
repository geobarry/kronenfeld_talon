app: Microsoft Word
app-name:
-
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
	insert(number_1)
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
	insert(number_1)
	insert(" approximately here>")


table <number> here:
	insert("<table ")
	insert(number_1)
	insert(" approximately here>")