# Maths Operations
3 + 5
7 - 4
3 * 2
6 / 3
2 ** 3 # 2^3

# PEMDASLR (Parentheses, Exponents, Multiply & Divide, Add & Subtract, Left to Right)
# ()
# **
# * /
# + -

# Rounding
num = 8 / 3
print(num)
print(int(num))
print(round(num))

# Floor division: returns an integer not a float
print(8 // 3)

#Shorthand Operators
# a += 2  short for a = a + 2
# -=
# *=
# /=
result = 4 / 2
result /= 2 # result = result / 2
print(result)

# f-string
score = 42
# print("Your score is " + score) # Type error
print("Your score is " + str(score)) # Inconvinient
height = 1.8
isWinning = True

print(f"Your score is {score}, your height is {height}, are you winning? {isWinning}")
