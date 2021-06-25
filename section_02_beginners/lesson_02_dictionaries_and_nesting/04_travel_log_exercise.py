# You are going to write a program that adds to a travel_log. You can see travel_log which
# is a List that contains 2 Dictionaries.
# Write a function that will work with the following line of code to add the entry for Russia
# to the travel_log.
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# You've visited Russia 2 times.
# You've been to Moscow and Saint Petersburg.
# DO NOT modify the travel_log directly. You need to create a function that modifies it.

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
def add_new_country(country, num_of_visits, cities_visited):
    travel_log.append({
        "country": country,
        "visits": num_of_visits,
        "cities": cities_visited,
    })

# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
