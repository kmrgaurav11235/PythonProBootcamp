import pandas

data = pandas.read_csv(filepath_or_buffer="weather_data.csv")
# print(data)
print(type(data))  # DataFrame: https://pandas.pydata.org/docs/reference/frame.html

print("\nTemperature data:")
# print(data["temp"])
print(type(data["temp"]))  # Series: https://pandas.pydata.org/docs/reference/series.html

# Convert DataFrame to dict:
data_dict = data.to_dict()
print(data_dict)

# Convert Series to list
temp_list = data["temp"].to_list()
print(temp_list)

# average_temp = round(sum(temp_list) / len(temp_list), 2)
average_temp = round(data["temp"].mean(), 2)  # Using the mean method in Series
print(f"Average Temperature: {average_temp}")

max_temp = data["temp"].max()
print(f"Max Temperature: {max_temp}")

# Pandas library converts each of the column into attributes of DataFrame
print(data.condition)

# Get data in rows
monday_row = data[data.day == "Monday"]
# monday_row = data[data["day"] == "Monday"] # Also works
print(monday_row)
print(type(monday_row))  # DataFrame

# Which day had the highest temperature in the week?
max_temp = data.temp.max()
max_temp_day = data[data.temp == max_temp]
print(max_temp_day)
print(f"Conditions of max temperature day = {max_temp_day.condition}")

# Convert Monday's temperature from Celsius to Fahrenheit
monday_temp_celsius = data[data.day == "Monday"].temp.item()
# monday_temp_celsius = int(data[data.day == "Monday"].temp)  # alternative
monday_temp_fahrenheit = (9 * monday_temp_celsius / 5) + 32
print(f"Monday temperature: Celsius {monday_temp_celsius}, Fahrenheit = {monday_temp_fahrenheit}")

# Create a DataFrame from scratch
data_dict = {
    "students": ["Guts", "Griffith", "Casca"],
    "scores": [76, 56, 65],
}

imported_data = pandas.DataFrame(data=data_dict)
print(imported_data)

# Convert DataFrame to csv file
imported_data.to_csv(path_or_buf="Berserk.csv")
