# ----------------- Question 1 -----------------
# You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain
# every number in the list numbers but each number should be squared.
# e.g. 4 * 4 = 16
# 4 squared equals 16.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:

squared_numbers = [num ** 2 for num in numbers]

# Write your code 👆 above:

print(squared_numbers)

# ----------------- Question 2 -----------------
# You are going to write a List Comprehension to create a new list called result. This new list should only contain the
# even numbers from the list numbers.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

# Write your 1 line code 👇 below:

result = [num for num in numbers if num % 2 == 0]

# Write your code 👆 above:

print(result)

# ----------------- Question 3 -----------------
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.
# IMPORTANT: The result should be a list that contains Integers, not Strings.


# Write your code 👇 below

with open(file="file1.txt") as file1:
    file1_list = file1.readlines()

with open(file="file2.txt") as file2:
    file2_list = file2.readlines()

file1_num_list = [int(item.strip()) for item in file1_list]
file2_num_list = [int(item.strip()) for item in file2_list]

result = [num for num in file1_num_list if num in file2_num_list]

# Write your code above 👆

print(result)

