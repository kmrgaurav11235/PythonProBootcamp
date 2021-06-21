def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# Positional Arguments - order is important
# greet_with("Ar-Pharazôn", "Númenor")

# Keyword Arguments - order is not important
greet_with(location="Númenor", name="Ar-Pharazôn")