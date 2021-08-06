# 1
# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the
# given sentence and calculates the number of letters in each word.
# Try Googling to find out how to convert a sentence into a list of words.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
result = {word: len(word) for word in sentence.split()}

print(result)

# 2
# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in
# degrees Celsius and converts it into degrees Fahrenheit.
# To convert temp_c into temp_f:
# (temp_c * 9/5) + 32 = temp_f

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

# Write your code 👇 below:

weather_f = {day: (temperature_c * 9 / 5) + 32 for (day, temperature_c) in weather_c.items()}

print(weather_f)
