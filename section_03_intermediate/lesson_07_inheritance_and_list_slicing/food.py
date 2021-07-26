from turtle import Turtle
from random import randint


# Food inherits from turtle: Our food will be a small circular turtle that will not move
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # A normal turtle is 20px * 20px. This makes it 10px * 10px
        self.color("blue")

        # This means we don't have to look at the animation of food being created at the centre and then moving to
        # its location
        self.speed("fastest")

        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)

