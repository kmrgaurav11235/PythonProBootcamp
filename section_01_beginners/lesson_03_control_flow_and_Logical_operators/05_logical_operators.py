# Write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word 
# TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number. 
# For Love Scores **less than 10** or **greater than 90**, the message should be:
#   "Your score is **x**, you go together like coke and mentos."
# For Love Scores **between 40** and **50**, the message should be:
#   "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
#   "Your score is **z**."

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined = name1 + name2
combined_lower = combined.lower()

score1 = 0
score1 += combined_lower.count("t")
score1 += combined_lower.count("r")
score1 += combined_lower.count("u")
score1 += combined_lower.count("e")

score2 = 0
score2 += combined_lower.count("l")
score2 += combined_lower.count("o")
score2 += combined_lower.count("v")
score2 += combined_lower.count("e")

score = int(str(score1) + str(score2))

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")