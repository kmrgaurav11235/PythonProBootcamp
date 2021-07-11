from turtle import Turtle, Screen

timmy = Turtle()
# timmy => object, Turtle => class
# "." (dot) operator is used to access the attributes and methods of an object
print(timmy)  # prints the location of the object
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
