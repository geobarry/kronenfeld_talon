tag: user.python
-
loop on:
	user.insert_between('for ',' in :')
check if:
	user.insert_between('if ',' in :' )
slide over:
	key(end)
	edit.left()
whack:
	key('end')
	insert(':')
	edit.line_insert_down()
(absolute value)|(funk absolute):
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
select scope:
	code.extend_scope_out()

# variables
variable {user.variable_list}:
	insert(variable_list)
	
{user.variable_list} equals:
	insert(variable_list)
	insert(" = ")
	
for {user.variable_list} in:
	insert("for ")
	insert(variable_list)
	insert(" in ")

range length {user.variable_list}:
	insert("range(len(")
	insert(variable_list)
	insert("))")
	
if {user.variable_list}:
	insert("if ")
	insert(variable_list)

if length {user.variable_list}:
	insert("if len(")
	insert(variable_list)
	insert(")")

{user.variable_list} sub:
	insert(variable_list)
	user.insert_between("[","]")
	
range {user.variable_list}:
	insert("range(")
	insert(variable_list)
	insert(")")
range <number>:
	insert("range(")
	insert(number)
	insert(")")

return {user.variable_list}:
	insert("return ")
	insert(variable_list)
{user.variable_list} dot append:
	insert(variable_list)
	user.insert_between(".append(",")")