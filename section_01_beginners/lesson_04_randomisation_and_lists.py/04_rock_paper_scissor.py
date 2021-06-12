import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices_list = [rock, paper, scissors]

human_choice_int = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors. "))
human_choice = ""
if human_choice_int >= 0 and human_choice_int <= 2:
  human_choice = choices_list[human_choice_int]
else:
  print("Invalid Choice.")
  exit(1)
print("You chose:\n" + human_choice)

computer_choice = random.choice(choices_list)
print("Computer chose:\n" + computer_choice)

if human_choice == computer_choice:
  print("It's a tie!")
elif (human_choice == rock and computer_choice == paper) or (human_choice == paper and computer_choice == scissors) or (human_choice == scissors and computer_choice == rock):
  print("You lose!")
else:
  print("You win!")

