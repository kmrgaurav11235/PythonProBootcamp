# Nesting a list in a dictionary
travel_log = {
    "Crownlands": ["King's Landing", "Dragonstone"],
    "The North": ["Winterfell", "White Harbor", "Last Hearth"],
}

# Nesting a list in a list
parties_of_war = ["Baratheon", ["Stark", "Tully"], ["Lannister", "Tyrell"], "Greyjoy"]

# Nesting a dictionary in a dictionary
travel_log = {
    "Crownlands": {
        "cities_visited": ["King's Landing", "Dragonstone"],
        "total_visits": 12,
    },
    "The North": {
        "cities_visited": ["Winterfell", "White Harbor", "Last Hearth"],
        "total_visits": 9,
    },
}

# Nesting a dictionary in a list
travel_log = [
    {
        "kingdom": "Crownlands",
        "cities_visited": ["King's Landing", "Dragonstone"],
        "total_visits": 12,
    },
    {
        "kingdom": "The North",
        "cities_visited": ["Winterfell", "White Harbor", "Last Hearth"],
        "total_visits": 9,
    },
]
