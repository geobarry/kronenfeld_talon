from talon import Context, Module, app, storage
import csv
import os
from pathlib import Path
from collections import OrderedDict

from talon import resource

# NOTE: This method requires list csv files to be in same directory or subdirectory of this directory

BASE_DIR = Path(__file__).parent


mod = Module()
mod.list("variable_list", desc="saved variable name abbreviations")
mod.list("person_list", desc="saved person names")
mod.list("module_list", desc="saved module names")
mod.list("function_list", desc="saved function names")
mod.list("keyword_list", desc="saved keyword names")
mod.list("app_list", desc="saved app names")

ctx = Context()
variable_list = {}
person_list = {}
module_list = {}
function_list = {}
keyword_list = {}
app_list = {}

@mod.action_class
class Actions:
    def write_list(rel_file_path: str, list_name: str):
        """write contents of list to a csv file"""
        list = storage.get(list_name, {})        
        append_to_csv(rel_file_path,list)
    def save_to_list(rel_file_path: str, spoken: str, text: str):
        """save a new variable to user.variable_list"""
        D = {spoken:text}
        append_to_csv(rel_file_path,D)
#        variable_list = storage.get("variable_list", {})
#        variable_list[spoken] = text
#        ctx.lists["user.variable_list"] = variable_list
#        storage.set("variable_list", variable_list)

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


def get_list_from_csv(
    rel_file_path: str, headers: tuple[str, str], default: dict[str, str] = {}
):
    """Retrieves list from CSV"""
    path = BASE_DIR / rel_file_path
    assert rel_file_path.endswith(".csv")

    if not path.is_file():
        with open(path, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for key, value in default.items():
                writer.writerow([key] if key == value else [value, key])

    # Now read via resource to take advantage of talon's
    # ability to reload this script for us when the resource changes
    with resource.open(str(path), "r") as f:
        rows = list(csv.reader(f))

    # print(str(rows))
    mapping = {}
    if len(rows) >= 2:
        actual_headers = rows[0]
        if not actual_headers == list(headers):
            print(
                f'"{rel_file_path}": Malformed headers - {actual_headers}.'
                + f" Should be {list(headers)}. Ignoring row."
            )
        for row in rows[1:]:
            if len(row) == 0:
                # Windows newlines are sometimes read as empty rows. :champagne:
                continue
            if len(row) == 1:
                output = spoken_form = row[0]
            else:
                output, spoken_form = row[:2]
                if len(row) > 2:
                    print(
                        f'"{rel_file_path}": More than two values in row: {row}.'
                        + " Ignoring the extras."
                    )
            # Leading/trailing whitespace in spoken form can prevent recognition.
            spoken_form = spoken_form.strip()
            mapping[spoken_form] = output

    return mapping


def append_to_csv(rel_file_path: str, rows: dict[str, str]):
    path = BASE_DIR / rel_file_path
    assert rel_file_path.endswith(".csv")

    with open(str(path)) as file:
        line = None
        for line in file:
            pass
        needs_newline = line is not None and not line.endswith("\n")
    with open(path, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        if needs_newline:
            writer.writerow([])
        d = OrderedDict(sorted(rows.items(), key=lambda t: t[1].upper()))
        for key, value in d.items():
            writer.writerow([key] if key == value else [value, key])

def on_ready():
    variable_list = get_list_from_csv(
        "lists\\variables.csv",
        headers=("Variable", "Spoken Form")
    )
    ctx.lists["user.variable_list"] = variable_list
    # global person_list
    #person_list = storage.get("person_list", {})
    person_list = get_list_from_csv(
        "lists\\persons.csv",
        headers=("Name", "Spoken Form")
    )
    ctx.lists["user.person_list"] = person_list
    # global module_list
    #module_list = storage.get("module_list", {})
    module_list = get_list_from_csv(
        "lists\\modules.csv",
        headers=("Module Name", "Spoken Form")
    )
    ctx.lists["user.module_list"] = module_list
    # global function_list
#    function_list = storage.get("function_list", {})
    function_list = get_list_from_csv(
        "lists\\functions.csv",
        headers=("Function", "Spoken Form")
    )
    ctx.lists["user.function_list"] = function_list
    # global keyword_list
#    keyword_list = storage.get("keyword_list", {})
    keyword_list = get_list_from_csv(
        "lists\\keywords.csv",
        headers=("Keyword", "Spoken Form")
    )
    ctx.lists["user.keyword_list"] = keyword_list
    # global app_list
#    app_list = storage.get("app_list", {})
    app_list = get_list_from_csv(
        "lists\\apps.csv",
        headers=("App Name", "Spoken Form")
    )
    ctx.lists["user.app_list"] = app_list

app.register("ready", on_ready)
