from turtle import Turtle

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Player 1: {self.left_score}", align="center", font=("Courier", 20, "normal"))
        self.goto(200, 250)
        self.write(f"Player 2: {self.right_score}", align="center", font=("Courier", 20, "normal"))

    def point_left(self):
        self.left_score += 1
        self.update_score()

    def point_right(self):
        self.right_score += 1
        self.update_score()
