from art import logo
from art import vs
from game_data import data
from random import choice

# Initialize score
score = 0

continue_game = True
first_entity = choice(data)
print(logo)

while continue_game:
    # Fetch data from list and Pick two random data
    second_entity = choice(data)

    # Store the correct choice
    if first_entity['follower_count'] > second_entity['follower_count']:
        correct_choice_entity = first_entity
    else:
        correct_choice_entity = second_entity
    print(f"Correct choice: {correct_choice_entity}")

    # Display 1 vs 2
    print(f"Compare A: {first_entity['name']}, a {first_entity['description']} from {first_entity['country']}")
    print(vs)
    print(f"Against B: {second_entity['name']}, a {second_entity['description']} from {second_entity['country']}")
    # Get user input
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Check if user is right - if yes loop, if no show end message
    if user_choice == "A":
        user_choice_entity = first_entity
    elif user_choice == "B":
        user_choice_entity = second_entity
    else:
        print("Invalid Choice!")
        continue_game = False

    print(logo)
    if user_choice_entity == correct_choice_entity:
        score += 1
        print(f"You're right! Current score: {score}.")
        first_entity = second_entity
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        continue_game = False
