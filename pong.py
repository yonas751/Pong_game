from turtle import Turtle

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, -200)
        self.x_move = -10  # Start going left
        self.y_move = 10   # Start going up
        self.move_speed = 5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_down(self):
        self.y_move = -abs(self.y_move)  # Always bounce downward

    def bounce_up(self):
        self.y_move = abs(self.y_move)

    def change_direction(self):
        self.x_move *= -1  # Switch left ↔ right

    def reset_position(self):
        self.goto(0, -200)
        self.move_speed = 0.05
        self.x_move = -10  # Always start toward left again
        self.y_move = 10


