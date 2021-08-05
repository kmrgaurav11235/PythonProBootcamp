numbers = [1, 2, 3]

# Without List Comprehension
new_list = []
for num in numbers:
    new_list.append(num + 1)

# List Comprehension
# new_list = [new_item for item in list]
new_list = [num + 1 for num in numbers]

print(new_list)

# List Comprehension also works with other sequences, e.g. Strings
name = "Saitama"
new_list = [letter for letter in name]
print(new_list)

# list, range, string, tuple etc. are called Sequences in Python as they have a specific order.

# Create a list of all even numbers less than 10
even_num_list = [num * 2 for num in range(1, 5)]
print(even_num_list)

# Conditional List Comprehension
# new_list = [new_item for item in list if test]
supes_list = ["Homelander", "Black Noir", "Queen Maeve", "A-Train", "The Deep", "Lamplighter", "Starlight", "Stormfront"]
long_name_supes = [name for name in supes_list if len(name) >= 10]
print(long_name_supes)
