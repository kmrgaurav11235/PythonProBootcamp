# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short 
# person both weigh the same amount, the short person is usually more overweight
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# Example Input
# weight = 80
# height = 1.75

# Calculation
# 80 ÷ (1.75 x 1.75) =  26.122448979591837

# Example Output
# 26

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi_float = float(weight) / (float(height) ** 2)
bmi_int = int(bmi_float)
print(bmi_int)