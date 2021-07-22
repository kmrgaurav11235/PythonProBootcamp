from turtle import Turtle, Screen
from random import randint

window_width = 500
window_height = 400
is_race_on = False

screen = Screen()

# Since the size of window is important, we will not use the default size
screen.setup(width=window_width, height=window_height)

user_choice = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ").lower()

turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple", "violet"]
num_turtles = len(turtle_colors)

# Turtles are 40px wide
turtle_x_coordinate = (- window_width / 2) + 20  # Adding '20', so that the turtle doesn't goes off-screen
finish_line = (window_width / 2) - 20
vertical_step = int(window_height / (num_turtles + 1))
sign = 1
multiplying_factor = 0

turtle_list = []
for turtle_color in turtle_colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()

    turtle_y_coordinate = sign * multiplying_factor * vertical_step
    if sign == 1:
        sign = -1
        multiplying_factor += 1
    elif sign == -1:
        sign = 1

    new_turtle.goto(x=turtle_x_coordinate, y=turtle_y_coordinate)
    new_turtle.color(turtle_color)
    turtle_list.append(new_turtle)

if user_choice:
    is_race_on  = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > finish_line:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
        forward = randint(0, 10)
        turtle.forward(forward)
