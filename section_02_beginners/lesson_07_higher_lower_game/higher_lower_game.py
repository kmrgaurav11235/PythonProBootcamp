from art import logo
from art import vs
from game_data import data
from random import choice

# Initialize score
score = 0

# Fetch data from list and Pick two random data
entity1 = choice(data)
entity2 = choice(data)

# Store the correct choice
if entity1['follower_count'] > entity2['follower_count']:
    correct_choice_entity = entity1
else:
    correct_choice_entity = entity2
print(f"Correct choice: {correct_choice_entity}")

# Display 1 vs 2
print(logo)
print(f"Compare A: {entity1['name']}, a {entity1['description']} from {entity1['country']}")
print(vs)
print(f"Against B: {entity2['name']}, a {entity2['description']} from {entity2['country']}")
# Get user input
user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

# Check if user is right - if yes loop, if no show end message
if user_choice == "A":
    user_choice_entity = entity1
elif user_choice == "B":
    user_choice_entity = entity2
else:
    print("Wrong Choice")

if user_choice_entity == correct_choice_entity:
    score += 1
    print(f"You're right! Current score: {score}.")
else:
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}.")
