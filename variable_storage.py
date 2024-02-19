from talon import Context, Module, app, storage

mod = Module()
mod.list("variable_list", desc="saved variable name abbreviations")
mod.list("person_list", desc="saved person names")
mod.list("module_list", desc="saved module names")
mod.list("function_list", desc="saved function names")
mod.list("keyword_list", desc="saved keyword names")
mod.list("app_list", desc="saved app names")

ctx = Context()
variable_list = {}
module_list = {}
function_list = {}
keyword_list = {}
app_list = {}

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

    def save_keyword(spoken: str, text: str):
        "save a new keyword name to user.function_list"
        keyword_list = storage.get("keyword_list", {})
        keyword_list[spoken] = text
        ctx.lists["user.keyword_list"] = keyword_list
        storage.set("keyword_list", keyword_list)

    def remove_keyword(spoken: str):
        "removed a keyword from user.keyword_list"
        keyword_list = storage.get("keyword_list", {})        
        del keyword_list[spoken]
        ctx.lists["user.keyword_list"] = keyword_list
        storage.set("keyword_list", keyword_list)

    def save_app(spoken: str, text: str):
        "save a new app name to user.function_list"
        app_list = storage.get("app_list", {})
        app_list[spoken] = text
        ctx.lists["user.app_list"] = app_list
        storage.set("app_list", app_list)

    def remove_app(spoken: str):
        "removed a app from user.app_list"
        app_list = storage.get("app_list", {})        
        del app_list[spoken]
        ctx.lists["user.app_list"] = app_list
        storage.set("app_list", app_list)


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
    # global keyword_list
    keyword_list = storage.get("keyword_list", {})
    ctx.lists["user.keyword_list"] = keyword_list
    # global app_list
    app_list = storage.get("app_list", {})
    ctx.lists["user.app_list"] = app_list



app.register("ready", on_ready)