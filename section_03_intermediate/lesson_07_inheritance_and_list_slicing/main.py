from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # This turns the tracer off. Now the screen will refresh only after screen.update() is called

snake = Snake()

is_game_on = True
while is_game_on:
    screen.update()  # Updates the screen only after all the segments have moved.
    time.sleep(0.1)  # Sleeps for 0.1 seconds. This controls the pace of the snake

    snake.move()

screen.exitonclick()
