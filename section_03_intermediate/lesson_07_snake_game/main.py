from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Snake body: we will create 3 turtles as squares -- lined up with each other.
# Body of a turtle is 20px * 20px -- centered at (0, 0) by default
turtle_width = 20
turtles = []
for index in range(3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    turtle_x_coordinate = index * turtle_width * -1
    new_turtle.setposition(x=turtle_x_coordinate, y=0)
    turtles.append(new_turtle)

screen.exitonclick()
