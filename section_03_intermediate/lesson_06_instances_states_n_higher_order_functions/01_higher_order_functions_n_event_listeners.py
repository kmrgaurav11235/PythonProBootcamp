from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


screen.listen()  # Start listening to events
# Higher order functions take other functions as arguments
screen.onkey(move_forward, "space")  # When we use a function as an argument, we don't add the parenthesis
screen.exitonclick()
