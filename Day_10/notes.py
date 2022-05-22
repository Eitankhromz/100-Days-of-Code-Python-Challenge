#Function with outputs

def format_name(f_name, l_name):
    """Take a first and last name and format it to return a title case version"""
    if f_name == "" or l_name =="":
        return "You didn't provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Return: {formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))
