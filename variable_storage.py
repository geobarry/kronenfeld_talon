from talon import Context, Module, app, storage

mod = Module()
mod.list("variable_list", desc="saved variable name abbreviations")
mod.list("person_list", desc="saved person names")
mod.list("module_list", desc="saved module names")
mod.list("function_list", desc="saved function names")

ctx = Context()
variable_list = {}
module_list = {}
function_list = {}

@mod.action_class
class Actions:
    def save_variable(spoken: str, text: str):
        "save a new variable to user.variable_list"
        variable_list = storage.get("variable_list", {})
        variable_list[spoken] = text
        ctx.lists["user.variable_list"] = variable_list
        storage.set("variable_list", variable_list)

    def remove_variable(spoken: str):
        "removed a variable from user.variable_list"
        variable_list = storage.get("variable_list", {})        
        del variable_list[spoken]
        ctx.lists["user.variable_list"] = variable_list
        storage.set("variable_list", variable_list)

    def save_person(spoken: str, text: str):
        "save a new person to user.person_list"
        person_list = storage.get("person_list", {})
        person_list[spoken] = text
        ctx.lists["user.person_list"] = person_list
        storage.set("person_list", person_list)

    def remove_person(spoken: str):
        "removed a person from user.person_list"
        person_list = storage.get("person_list", {})        
        del person_list[spoken]
        ctx.lists["user.person_list"] = person_list
        storage.set("person_list", person_list)

    def save_module(spoken: str, text: str):
        "save a new module name to user.module_list"
        module_list = storage.get("module_list", {})
        module_list[spoken] = text
        ctx.lists["user.module_list"] = module_list
        storage.set("module_list", module_list)

    def remove_module(spoken: str):
        "removed a module from user.module_list"
        module_list = storage.get("module_list", {})        
        del module_list[spoken]
        ctx.lists["user.module_list"] = module_list
        storage.set("module_list", module_list)

    def save_function(spoken: str, text: str):
        "save a new function name to user.function_list"
        function_list = storage.get("function_list", {})
        function_list[spoken] = text
        ctx.lists["user.function_list"] = function_list
        storage.set("function_list", function_list)

    def remove_function(spoken: str):
        "removed a function from user.function_list"
        function_list = storage.get("function_list", {})        
        del function_list[spoken]
        ctx.lists["user.function_list"] = function_list
        storage.set("function_list", function_list)



def on_ready():
    # global variable_list
    variable_list = storage.get("variable_list", {})
    ctx.lists["user.variable_list"] = variable_list
    # global person_list
    person_list = storage.get("person_list", {})
    ctx.lists["user.person_list"] = person_list
    # global module_list
    module_list = storage.get("module_list", {})
    ctx.lists["user.module_list"] = module_list
    # global function_list
    function_list = storage.get("function_list", {})
    ctx.lists["user.function_list"] = function_list



app.register("ready", on_ready)