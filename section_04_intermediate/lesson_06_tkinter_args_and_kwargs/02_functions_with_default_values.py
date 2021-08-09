# b and c have a default value of 6
def foo(a, b=4, c=6):
    print(a, b, c)


foo(1)  # Prints: 1 4 6
foo(4, 9)  # Prints: 4 9 6
foo(1, 7, 9)  # Prints: 1 7 9
foo(20, c=6)  # Prints: 20 4 6

import turtle

screen = turtle.Screen()

tim = turtle.Turtle()
# The definition of write method looks like this:
# def write(self, arg, move=False, align="left", font=("Arial", 8, "normal")):
tim.write(arg="Write this.", font=("Arial", 24, "bold"))  # Except 'arg' all parameters have default values

screen.exitonclick()
