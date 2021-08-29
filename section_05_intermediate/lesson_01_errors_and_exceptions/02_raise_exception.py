# We  can raise exception using the 'raise' keyword
height = float(input("Enter your height (in meters): "))
weight = float(input("Enter your weight (in kg): "))

if height > 3.0:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(f"Your bmi is: {bmi}")
