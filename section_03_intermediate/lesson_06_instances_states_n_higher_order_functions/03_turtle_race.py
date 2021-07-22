from turtle import Turtle, Screen

window_width = 500
window_height = 400

screen = Screen()

# Since the size of window is important, we will not use the default size
screen.setup(width=window_width, height=window_height)

user_choice = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
print(user_choice)

turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple", "violet"]
num_turtles = len(turtle_colors)

turtle_x_coordinate = (- window_width / 2) + 20  # Adding '20', so that the turtle doesn't goes off-screen
vertical_step = int(window_height / (num_turtles + 1))
sign = 1
multiplying_factor = 0

turtles = []
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
    turtles.append(new_turtle)

screen.exitonclick()
