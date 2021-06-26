# Functions with outputs
def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return "You didn't provide valid inputs"
        # Multiple returns are allowed in the same method
        # return with nothing following it -> Returns a 'None'

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"
    # This print statement will never get executed as it comes after return
    print("This is unreachable")


formatted_string = format_name("eLu", "ThiNgOl")
print(formatted_string)
