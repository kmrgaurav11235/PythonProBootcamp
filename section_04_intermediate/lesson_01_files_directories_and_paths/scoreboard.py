from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
DATA_FILE = "data.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score_from_data_file()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def read_high_score_from_data_file(self):
        with open(file=DATA_FILE) as data_file:
            high_score = data_file.read()
            return int(high_score)

    def write_high_score_to_data_file(self, score):
        with open(file=DATA_FILE, mode="w") as data_file:
            data_file.write(str(score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score_to_data_file(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
