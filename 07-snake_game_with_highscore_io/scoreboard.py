import os
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.load_high_score_from_file()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=True, align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def save_high_score_to_file(self):
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))

    def load_high_score_from_file(self):
        if os.path.exists("high_score.txt"):
            with open("high_score.txt", mode="r") as file:
                self.high_score = int(file.read())

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score_to_file()
        self.score = 0
        self.update_scoreboard()
