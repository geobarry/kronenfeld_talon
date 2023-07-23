tag: user.python
-
loop on:
	user.insert_between('for ',' in :')
slide over:
	key(end)
	edit.left()
whack:
	key('end')
	insert(':')
	edit.line_insert_down()
absolute value:
	insert('abs')
	user.engine_mimic('args')
set equal [to]:
	user.engine_mimic('op equals')
funk sign:
	insert('math.sin()')
	edit.left()
funk cosine:
	insert('math.cos()')
	edit.left()
funk radians:
	insert('math.radians()')
	edit.left()
funk max:
	insert('max()')
	edit.left()
funk admin:
	insert('min()')
	edit.left()
algebra (minus|subtract):
	user.code_operator_subtraction()
algebra (times|multiply):
	user.code_operator_multiplication()
algebra (plus|add):
	user.code_operator_addition()
algebra (divide):
	user.code_operator_division()
algebra (mod|modulus):
	user.code_operator_modulo()
hello world: "hello world"