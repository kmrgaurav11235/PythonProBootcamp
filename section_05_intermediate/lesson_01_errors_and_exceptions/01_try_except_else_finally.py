# my_list = [1, 1, 2, 3, 5]
# print(my_list[5])  # Throws IndexError: list index out of range
#
# print(1 + "abc")  # Throws TypeError: unsupported operand type(s) for +: 'int' and 'str'
try:
    # 'try' contains code that can throw an exception
    file_name = "a_file.txt"
    text_file = open(file_name)  # Throws FileNotFoundError: No such file or directory: 'a_file.txt'

    my_dict = {"key1": "value1"}
    print(my_dict["key2"])  # Throws KeyError: 'key2'
except FileNotFoundError:
    # 'except' contains code to execute if the particular exception gets throws.
    print(f"Cannot open {file_name}. Creating new file.")
    text_file = open(file_name, "w")
    text_file.write("Something")
except KeyError as key_error_msg:
    # 'as' allows us to access the error message.
    print(f"{key_error_msg} key doesn't exists.")
else:
    # 'else' is executed if 'try' didn't throw any exception.
    print(text_file.read())
finally:
    # 'finally' is executed bo matter what happens
    text_file.close()
    print(f"{file_name} was closed.")
