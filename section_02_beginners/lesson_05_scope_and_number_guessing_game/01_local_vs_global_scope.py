################### Scope ####################

# Local Scope: Inside a function
def drink_potion0():
    potion_strength = 2
    print(potion_strength) # ok

# print(potion_strength) # Gives NameError: name 'potion' is not defined

# Global Scope: Outside function
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

# Python does not have "Block Scope"
game_level = 3
enemies = ["Skeleton", "Zombie", "Aliens"]
if game_level < 5:
  new_enemy = enemies[0]

print(new_enemy) # This is valid even though it was created inside the "if-condition". Same for loops.
# But if we put the creation of new_enemy inside a function, this will not work
# Thus, loops and conditions don't create a separate local scope. Only functions do.


