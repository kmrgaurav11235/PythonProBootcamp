################### Scope ####################

# Local Scope
def drink_potion0():
    potion_strength = 2
    print(potion_strength) # ok

# print(potion_strength) # Gives NameError: name 'potion' is not defined

# Global Scope
player_health = 10
def drink_potion1():
    print(player_health) # ok

print(player_health) # Also ok

# This concept of global and local doesn't just applies to variables, it also applies to 
# functions. This concept is called namespace.

# Local and Global variables are distinct

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}") # Prints 2

increase_enemies()
print(f"enemies outside function: {enemies}") # Prints 1
