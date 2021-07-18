from turtle import Turtle, Screen
from random import randint, choice

tim = Turtle()
tim.pensize(10)
tim.speed("fastest")
screen = Screen()
screen.colormode(255)
directions = [0, 90, 180, 270]

for _ in range(200):
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    tim.color(random_color)
    random_direction = choice(directions)
    tim.setheading(random_direction)
    tim.forward(50)

screen.exitonclick()
