from random import choice
from turtle import Turtle, Screen

tim = Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()  # Don't need pendown to draw a dot
tim.setposition(-200, -200)
screen = Screen()
screen.colormode(255)


def get_random_color():
    color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
                  (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
                  (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171),
                  (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
                  (107, 127, 153), (174, 94, 97), (176, 192, 209)]  # From extract_colors.py
    return choice(color_list)


def draw_dot(dot_size):
    color = get_random_color()
    tim.dot(dot_size, color)


rows = 10
columns = 10
distance = 50
size = 20
for _ in range(columns):
    for _ in range(rows):
        draw_dot(size)
        tim.forward(distance)
    tim.setheading(90)
    tim.forward(distance)
    tim.setheading(180)
    tim.forward(distance * rows)
    tim.setheading(0)

screen.exitonclick()
