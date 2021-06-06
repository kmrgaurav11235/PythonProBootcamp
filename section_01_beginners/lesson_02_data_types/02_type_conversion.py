num_char = len(input("Enter your name: "))
print(num_char)

# print("Your name has " + num_char + " number of characters.") 
# TypeError: can only concatenate str (not "int") to str

# Type Function
print(type(num_char))

# Type Conversion
num_char_string = str(num_char)
print("Your name has " + num_char_string + " number of characters.") 

a = 10
print(type(float(a)))

print (70 + float(100.5))

print(str(100) + str(11))