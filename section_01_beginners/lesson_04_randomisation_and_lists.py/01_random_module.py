import random

random_integer = random.randint(1, 10)
print(random_integer)

# random float between [0.0 and 1.0)
random_float = random.random()
print(random_float)

# random float between [0.0 and 5.0)
random_float *= 5
print(random_float)

# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
coin_toss = random.randint(0, 1)
if coin_toss == 0:
  print("Heads")
else:
  print("Tails")