states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts"]

print(states_of_america[4])
# Negative index
print(states_of_america[-1])

# Modification
states_of_america[2] = "Maryland"
print(states_of_america)

# Append
states_of_america.append("South Carolina")
print("\nNew List:")
print(states_of_america)

# More about lists: https://docs.python.org/3/tutorial/datastructures.html

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# Extend
dirty_dozen.extend(["Mangoes", "Tomatoes"])

print(dirty_dozen)

# You are going to write a program which will select a random name from a list of names. 
# # The person selected will have to pay for everybody's food bill.
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
random_index = random.randint(0, len(names) - 1)
print(f"{names[random_index]} is going to buy the meal today!")

# Using the choice method
print("Random state: " + random.choice(states_of_america))



