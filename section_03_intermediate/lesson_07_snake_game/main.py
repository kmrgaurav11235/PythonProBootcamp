from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # This turns the tracer off. Now the screen will refresh only after screen.update() is called

# Snake body: we will create 3 turtles as squares -- lined up with each other.
# Body of a turtle is 20px * 20px -- centered at (0, 0) by default
turtle_width = 20
snake_segments = []
for index in range(3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    turtle_x_coordinate = index * turtle_width * -1
    new_turtle.setposition(x=turtle_x_coordinate, y=0)
    snake_segments.append(new_turtle)

is_game_on = True
while is_game_on:
    screen.update()  # Updates the screen only after all the segments have moved.
    time.sleep(0.1)  # Sleeps for 0.1 seconds. This controls the pace of the snake

    # Instead of just moving all three segments forward, we will do this:
    # 1. Move the 3rd segment to where the 2nd segment was.
    # 2. Move the 2nd segment to where the 1st segment was.
    # 3. Move the 1st segment forward.
    # This will allow our snake to make turns correctly
    for segment_num in range(len(snake_segments) - 1, 0, -1):
        # start = last segment, stop = 0, range = -1
        new_x = snake_segments[segment_num - 1].xcor()
        new_y = snake_segments[segment_num - 1].ycor()
        snake_segments[segment_num].goto(new_x, new_y)

    snake_segments[0].forward(20)

screen.exitonclick()
