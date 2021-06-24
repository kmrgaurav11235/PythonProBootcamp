programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.", # The last comma is optional
}

print(programming_dictionary["Bug"])
# print(programming_dictionary["Bog"]) # KeyError

# Keys and Values can be of different types within the same dictionary
my_dict = {
    "message": "hi",
    123: 14.2,
}
print(my_dict["message"])
print(my_dict[123])

# Add new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Create Empty dictionary
kings_of_cities = {}
kings_of_cities["Nargothrond"] = "Finrod Felagund"

# Edit an item in a dictionary
kings_of_cities["Nargothrond"] = "Orodreth"
print(kings_of_cities)

# Wipe an existing dictionary
kings_of_cities = {}
print(kings_of_cities)

# Loop through a dictionary
for item in programming_dictionary:
    print(item) # This just prints the keys
