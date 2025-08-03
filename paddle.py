from turtle import Turtle

STARTING_POSITIONS = [(-380, 0), (-380, 20), (-380, 40)]
MOVE_DISTANCE = 40


class Paddle:
    def __init__(self):
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.shapesize(stretch_wid=1, stretch_len=1)
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def up(self):
        for segment in self.segments:
            new_y = segment.ycor() + MOVE_DISTANCE
            new_x = segment.xcor()
            segment.goto(new_x , new_y)

    def down(self):
        for segment in self.segments:
            new_y = segment.ycor() - MOVE_DISTANCE
            new_x = segment.xcor()
            segment.goto(new_x , new_y)







