from talon import Context,Module,actions,ui
mod = Module()
mod.tag("excel_powerpoint_shared", desc="keyboard sequences that work in both excel and powerpoint")
mod.list("power_go_to_target", "places we can go in powerpoint with the f6 button")
mod.list("power_selection_target", "places we can go in powerpoint with the tab button")
mod.list("excel_number_format","formats in the dropdown on the main menu")

@mod.action_class
class Actions:
    def office_enable_editing():
        """Enables editing in Microsoft word when it opens up in Protected Mode"""
        prop_dict = [("name","Enable Editing")]
        actions.user.invoke_matching_element(prop_dict)

    def power_object_menu():
        """opens the menu associated with the current object"""
        actions.key("alt j")
        elements = actions.user.element_list()
        print(f"{len(elements)} elements found")
        for el in elements:
            if el.name == "Picture Tools":
                actions.key("p")                
                break
            elif el.name == "Shape Format":
                actions.key("d")
                break
            elif el.name == "Table Design":
                actions.key("l")
                break
            elif el.name == "Graphics Tools":
                actions.key("g")
                break
    def excel_set_number_format(excel_format: str):
        """sets the number format for selected cells"""
        actions.key("alt-h n alt-down")
        actions.user.key_to_matching_element("down",[("name",f"{excel_format}.*")],12)
        actions.key("enter")

    def unicode_word(unicode_code: str, font_name: str="Symbol"):
        """insert a unicode character into word"""
        def change_font(new_font):
            actions.key("alt-h")
            actions.sleep(0.05)
            actions.key("f:2")
            actions.sleep(0.1)
            actions.insert(new_font)
            actions.key("enter")
            actions.key("esc")
        # first change font to Times New Roman, otherwise strange things happen
        change_font("Times New Roman")
        # insert unicode
        actions.insert(unicode_code)
        actions.sleep(0.4)
        actions.key("alt-x")
        # change font
        actions.sleep(0.2)  
        actions.insert(" ")
        actions.edit.left()
        actions.edit.extend_left()
        actions.sleep(0.1)
        actions.key("alt-h")
        actions.sleep(0.05)
        actions.key("f:2")
        actions.sleep(0.1)
        actions.insert(font_name)
        actions.key("enter")
        actions.key("esc")
        actions.edit.right()
        actions.edit.right()
        actions.key("backspace")
    def unicode_excel_power(unicode_code: str, font_name: str="Times New Roman"):
        """insert a unicode character into excel or powerpoint"""
        actions.key("alt-n u alt-f")
        actions.insert(font_name)
        actions.sleep(0.1)
        actions.key("enter alt-m")
        # For most fonts the unicode hex is at the top
        actions.key("up:2")
        # For symbol fonts it is one down
        if font_name.upper() in ["SYMBOL", "WINGDINGS", "WINGDINGS 2", "WINDINGS 3"]:
            actions.key("down")
        actions.key("enter alt-c")
        actions.insert(unicode_code)
        actions.sleep(0.1)
        actions.key("alt-i tab enter")
    def go_excel_row_by_person(name: str, sleep_time: float = 0.1):
        """moves to the cell in the same row where the given person's name can be found"""
        # get column of current cell
        actions.key("alt-f3")
        actions.sleep(sleep_time*2)
        cur_cell = actions.edit.selected_text()
        col = "".join(x for x in cur_cell if not x.isdigit())
        print(f"col: {col}")
        actions.key("enter")
        actions.sleep(sleep_time*3)
        # use built-in search function to get row of cell with given name
        # NOTE: Need to set search parameters to search values not formulas
        actions.key("ctrl-f")
        actions.sleep(sleep_time)
        actions.insert(name)
        actions.sleep(sleep_time*3)
        actions.key("enter")
        actions.sleep(sleep_time*2)
        actions.key("esc")
        actions.sleep(sleep_time*2)
        actions.key("alt-f3 ctrl-a")
        actions.sleep(sleep_time*2)
        cur_cell = actions.edit.selected_text()
        row = "".join(x for x in cur_cell if x.isdigit())
        # navigate to row with name, current column
        actions.sleep(sleep_time)
        actions.insert(col + row)
        actions.sleep(sleep_time*2)
        actions.key("enter")
        actions.sleep(sleep_time)

    def power_tab_to(trg: str, occurrence: int = 1):
        """Presses tab until the target is reached"""
        print("FUNCTION: POWER TAB TO")
        el = ui.focused_element()
        print(f"1: {el.name}")
        orig_el = el
        instance_found = 0
        # press tab once if we are not moving to another element, try esc
        i=0
        actions.key("tab")
        last_el = el
        actions.sleep(0.1)
        el = ui.focused_element()
        print(f"2: {el.name}")
        while el.name == last_el.name and i < 5:
            print("Pressing tab but not moving, trying escape...")
            actions.key("ctrl-z esc tab")
            actions.sleep(0.1)
            last_el = el
            el = ui.focused_element()
            print(f"3: {el.name}")
            i += 1
        if trg.lower() in el.name.lower():
            instance_found += 1
        # look for target
        i = 0
        limit = 100        
        while instance_found != occurrence and i < limit:
            i += 1
            actions.key("tab")
            last_el = el
            el = ui.focused_element()
            print(f"4: {el.name}")
            if trg.lower() in el.name.lower():
                instance_found += 1
        # If target not found try going back to the beginning
        if not trg.lower() in el.name.lower():
            while el != orig_el and i < limit:
                i += 1
                actions.key("tab")
                el = ui.focused_element()
                print(f"5: {el.name}")
        

    def power_go_to(trg: str):
        """Presses F6 until the target (contents,slide,notes,menu) is reached"""
        def focused_element_type():
            
            el = ui.focused_element()
            print(el.name)
            if "Ribbon" in el.class_name:
                return "menu"
            elif "Slide Notes" in el.name:
                return "notes"
            elif el.name[:5] == "Slide":
                name_parts = el.name.split(" ")
                if len(name_parts) == 1:
                    return "contents"
                elif name_parts[1].isnumeric():
                    return "slide"
                else:
                    return "contents"
            elif el.name == "Play All" or el.name == "Animation Pane" \
                or el.name == "Move Up" or el.name == "Move Down":
                return "animation"            
            else:
                return ""
        print("FUNCTION: power_go_to")
        # prevent infinite cycling
        limit = 6
        i = 0
        # cycle until target is reached or else we have reached our limit
        start_type = focused_element_type()
        while focused_element_type() != trg and i < limit:
            i += 1
            actions.key("f6")
            
        # if target has not been reached, try to go back to where we came from
        if focused_element_type() != trg:
            i = 0
            while focused_element_type() != start_type and i < limit:
                i += 1
                actions.key("f6")
            
            
        
    def circle_number_excel_power(number: int):
        """insert a number inside a circle"""
        hex_code = "0080"
        integer_code = int(hex_code,16)
        integer_code += number
        hex_code = hex(integer_code)
        actions.user.unicode_excel_power(hex_code,"Wingdings")
    def dark_circle_number_excel_power(number: int):
        """insert a number inside a circle"""
        hex_code = "008B"
        integer_code = int(hex_code,16)
        integer_code += number
        hex_code = hex(integer_code)
        actions.user.unicode_excel_power(hex_code,"Wingdings")

    def letter_word(user_letter: str, a_hex_code: str, font_name: str="Times New Roman"):
        """insert one of a 26-letter unicode sequence of characters by english letter"""
        a_integer_code = int(a_hex_code,16) # unicode for equation font A
        user_letter_increment = ord(user_letter) - 97 # difference between user selected letter and a
        letter_integer_code = a_integer_code + user_letter_increment
        letter_hex_code = hex(letter_integer_code)[2:]
        actions.user.unicode_word(letter_hex_code,font_name)
        print(f"User stated letter: {user_letter} {ord(user_letter)} {letter_hex_code}")

    def equation_letter_word(user_letter: str):
        """insert a lower case letter inside a circle"""
        a_integer_code = int("1D44E",16) # unicode for equation font A
        user_letter_increment = ord(user_letter) - 97 # difference between user selected letter and a
        letter_integer_code = a_integer_code + user_letter_increment
        letter_hex_code = hex(letter_integer_code)[2:]
        actions.user.unicode_word(letter_hex_code,"Cambria Math")
        print(f"User stated letter: {user_letter} {ord(user_letter)} {letter_hex_code}")


    def circle_letter_word(user_letter: str):
        """insert a lower case letter inside a circle"""
        a_integer_code = int("24d0",16) # unicode for circled lowercase a
        user_letter_increment = ord(user_letter) - 97 # difference between user selected letter and a
        letter_integer_code = a_integer_code + user_letter_increment
        letter_hex_code = hex(letter_integer_code)[2:]
        actions.user.unicode_word(letter_hex_code,"times new roman")
        print(f"User stated letter: {user_letter} {ord(user_letter)} {letter_hex_code}")

ctx = Context()