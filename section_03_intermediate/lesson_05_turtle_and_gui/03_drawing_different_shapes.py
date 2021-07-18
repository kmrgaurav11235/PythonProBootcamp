from turtle import Turtle, Screen
from random import randint

tim = Turtle()
screen = Screen()
screen.colormode(255)


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for num_of_sides in range(3, 11):
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    tim.color(random_color, random_color)
    draw_shape(num_of_sides)

screen.exitonclick()
