import pandas

data = pandas.read_csv(filepath_or_buffer="weather_data.csv")
print(data)

print("\nTemperature data:")
print(data["temp"])