# Printing to Console
print("Hello World!")

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

print("Day 1 - String Manipulation")
print("String Concatenation is done with the \"+\" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

print(len(input("What is your name? ")))

# The Python input function
# input() will get user input in console
# Then print() will print the word "Hello" and the user input
print("Hello " + input("What is your name?"))

# Python Variables
name = input("What is your name?")
length = len(name)
print(length)

# Exercise: Switch values of variables
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c = a
a = b
b = c

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

# Band Name Generator

#1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")
#2. Ask the user for the city that they grew up in.
user_city = input("What's name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
user_pet_name = input("What's your pet's name?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be " + user_city + " " + user_pet_name)
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/