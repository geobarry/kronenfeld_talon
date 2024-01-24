from talon import Context,Module,actions
mod = Module()
mod.tag("excel_powerpoint_shared", desc="keyboard sequences that work in both excel and powerpoint")

@mod.action_class
class Actions:
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
        actions.key("alt-n")
        actions.key("u")
        actions.key("alt-f")
        actions.insert(font_name)
        actions.sleep(0.1)
        actions.key("enter")
        actions.key("alt-m")
        # For most fonts the unicode hex is at the top
        actions.key("up:2")
        # For symbol fonts it is one down
        if font_name.upper() in ["SYMBOL", "WINGDINGS", "WINGDINGS 2", "WINDINGS 3"]:
            actions.key("down")
        actions.key("enter")
        actions.key("alt-c")
        actions.insert(unicode_code)
        actions.sleep(0.1)
        actions.key("alt-i")
        actions.key("tab")
        actions.key("enter")
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
    def circle_letter_word(user_letter: str):
        """insert a lower case letter inside a circle"""
        a_integer_code = int("24d0",16) # unicode for circled lowercase a
        user_letter_increment = ord(user_letter) - 97 # difference between user selected letter and a
        letter_integer_code = a_integer_code + user_letter_increment
        letter_hex_code = hex(letter_integer_code)[2:]
        actions.user.unicode_word(letter_hex_code,"times new roman")
        print(f"User stated letter: {user_letter} {ord(user_letter)} {letter_hex_code}")

ctx = Context()