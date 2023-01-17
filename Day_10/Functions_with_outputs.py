# Functions with outputs

first = input("Please input first name:")
last = input("Please input last name:")

def format_name(f_name,l_name ):
    """This function takes first and last name and format it
        to return the title case version of name."""

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return("f{formated_f_name}{formated_l_name}")

print(format_name("AnGela","LE"))