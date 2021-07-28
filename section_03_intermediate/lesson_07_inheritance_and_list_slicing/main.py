from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # This turns the tracer off. Now the screen will refresh only after screen.update() is called

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Listen to key-strokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()  # Updates the screen only after all the segments have moved.
    time.sleep(0.15)  # Sleeps for 0.1 seconds. This controls the pace of the snake
    snake.move()

    # Detect collision with food: using the turtle distance() method
    if snake.head.distance(food) < 15:
        # Size of food = 10px. So, we put 15 here.
        food.refresh()
        snake.extend()
        scoreboard.increment_score()

    # Detect collision with wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        is_game_on = False
        scoreboard.game_over()

    # Detect collision with tail: If the head collides with any segment of snake, trigger 'game_over()'
    for segment in snake.snake_segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()


screen.exitonclick()
