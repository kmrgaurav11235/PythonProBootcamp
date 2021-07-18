from turtle import Turtle, Screen
from random import randint

tim = Turtle()
tim.speed("fastest")
screen = Screen()
screen.colormode(255)


def draw_spirograph(angle_in_degrees):
    steps = int(360 / angle_in_degrees)
    for _ in range(steps):
        random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
        tim.color(random_color)
        tim.circle(100)
        tim.left(angle_in_degrees)


draw_spirograph(5)
screen.exitonclick()
