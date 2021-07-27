from turtle import Turtle

FONT = ("Courier", 18, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.goto(x=0, y=270)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.refresh_score()
