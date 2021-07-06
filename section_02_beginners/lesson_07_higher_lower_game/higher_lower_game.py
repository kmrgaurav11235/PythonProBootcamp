from art import logo
from art import vs
from game_data import data
from random import choice

# Initialize score
score = 0

continue_game = True
first_entity = choice(data)
print(logo)

def format_entity(entity):
    """Takes the entity data and returns printable format."""
    return f"{entity['name']}, a {entity['description']}, from {entity['country']}"

def check_user_choice(num_followers_first, num_followers_second, user_choice):
    """Check if user is right - if yes loop, if no show end message"""
    if num_followers_first > num_followers_second:
        return user_choice == "A"
    elif num_followers_first < num_followers_second:
        return user_choice == "B"
    else:
        return True

while continue_game:
    # Fetch data from list and Pick two random data
    second_entity = choice(data)
    while first_entity == second_entity:
        second_entity = choice(data)

    # Store the correct choice
    if first_entity['follower_count'] > second_entity['follower_count']:
        correct_choice_entity = first_entity
    else:
        correct_choice_entity = second_entity
    print(f"Correct choice: {correct_choice_entity}")

    # Display 1 vs 2
    print(f"Compare A: {format_entity(first_entity)}")
    print(vs)
    print(f"Against B: {format_entity(second_entity)}")

    # Get user input
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    is_user_correct = check_user_choice(first_entity['follower_count'], second_entity['follower_count'], user_choice)

    print(logo)
    if is_user_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
        first_entity = second_entity
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        continue_game = False
