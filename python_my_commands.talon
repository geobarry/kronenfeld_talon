tag: user.my_python

-
line comment: insert("# ")
comment <user.text>: insert("# {text}")
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
set equal [to]:
	insert(" = ")
is equal [to]:
	insert(" == ")
[is] not equal [to]:
	insert(" != ")
[is] less then:
	insert(" < ")
[is] less than or equal [to]:
	insert(" <= ")
[is] greater than:
	insert(" > ")
[is] greater than or equal [to]:
	insert(" >= ")

# FUNCTIONS
define function: user.insert_between("def ",":")
	
# OPERATIONS
(operation|algebra) (minus|subtract): insert(" - ")
(operation|algebra) (times|multiply): insert(" * ")
(operation|algebra) (plus|add): insert(" + ")
(operation|algebra) (divide|over|divided by): insert(" / ")
(operation|algebra) (mod|modulus): insert(" % ")
(operation|algebra) squared: insert(" ** 2")
[(operation|algebra)] to the power of: insert(" ** ")
(operation increment|increment by): insert(" += ")
increment {user.variable_list} [by]: insert("{variable_list} += ")
(operation|algebra) square root: insert("**0.5")
square root [of] <number>: insert("{number} ** 0.5")
square root [of] {user.variable_list}: insert("{variable_list} ** 0.5")
select scope: code.extend_scope_out()

# INDICES
sub: user.insert_between("[","]")

# VARIABLES
variable {user.variable_list}: insert(variable_list)
{user.variable_list} comma {user.variable_list}: insert("{variable_list_1},{variable_list_2}")
{user.variable_list} equals: insert("{variable_list} = ")
{user.variable_list} plus equals: insert("{variable_list} += ")
{user.variable_list} is equal [to]: insert("{variable_list} == ")
{user.variable_list} is not equal [to]: insert("{variable_list} != ")
{user.variable_list} [is] greater than: insert("{variable_list} > ")
{user.variable_list} [is] greater than or equal: insert("{variable_list} >= ")
{user.variable_list} [is] less than: insert("{variable_list} < ")
{user.variable_list} [is] less than or equal: insert("{variable_list}  <= ")

for {user.variable_list} in: insert("for {variable_list} in ")
for {user.variable_list} in {user.variable_list}: insert("for {variable_list_1} in {variable_list_2}:")
while {user.variable_list}: insert("while {variable_list}")
if {user.variable_list}: insert("if {variable_list}")
if not {user.variable_list}: insert("if not {variable_list}")
if length {user.variable_list}: insert("if len({variable_list})")
length {user.variable_list}: insert("len({variable_list})")
range {user.variable_list}: insert("range({variable_list})")
range length {user.variable_list}: insert("range(len({variable_list}))")
range <number>: insert("range({number})")
{user.variable_list} sub: user.insert_between("{variable_list}[","]")
{user.variable_list} sub {user.variable_list}: insert("{variable_list_1}[{variable_list_2}]")
{user.variable_list} sub <number>: insert("{variable_list}[{number}]")
return {user.variable_list}: insert("return {variable_list}")
{user.variable_list} dot append: user.insert_between("{variable_list}.append(",")")
{user.variable_list} dot: insert("{variable_list}.")
unzip {user.variable_list}: insert("zip(*{user.variable_list})")
self dot {user.variable_list}: insert("self.{variable_list}")
	
string:
	user.insert_between('"','"')
raw string:
	user.insert_between('r"','"')
formatted string:
	user.insert_between('f"','"')	
unicode string:
	user.insert_between('u"','"')
dot format:
	user.insert_between(".format(",")")
dot split:
	user.insert_between(".split(",")>")
list:
	user.insert_between("[","]")
dictionary:
	user.insert_between("{","}")
tuple:
	user.insert_between("(",")")
empty list:
	insert("[]")
empty dictionary:
	insert("{}")
empty tuple:
	insert("()")


# modules
import {user.module_list}:
	insert("import ")
	insert(module_list)
from {user.module_list} import: 
	insert("from ")
	insert(module_list)
	insert(" import ")
from {user.module_list} import {user.module_list}:
	insert("from ")
	insert(module_list_1)
	insert(" import ")
	insert(module_list_2)
module {user.module_list}:
	insert(module_list)
module {user.module_list} dot:
	insert(module_list)
	insert(".")

# KEYWORDS
[python] keyword {user.keyword_list}:
	insert(keyword_list)

# FUNCTIONS
function {user.function_list}: user.insert_between("{function_list}(",")")
function name {user.function_list}: insert("{function_list}")

# numpy
numpy (linear|line) (space|spacing):
	user.insert_between("np.linspace(",")")