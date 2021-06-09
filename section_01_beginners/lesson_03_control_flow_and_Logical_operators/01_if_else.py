# Control Flow
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
else:
  print("Sorry, you have to grow taller before you ride.")

wants_photo = input("Do you want a photo taken? Y or N. ")
if wants_photo == "Y":
  bill += 3

print(f"Your final bill is ${bill}")

# Write a program that works out whether if a given number is an odd or even number.
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
