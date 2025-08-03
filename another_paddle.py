from turtle import Turtle, Screen

MOVE_DISTANCE = 20
TOP_LIMIT = 270
BOTTOM_LIMIT = -270

class AnotherPaddle:
    def __init__(self):
        self.segments = []
        self.direction = 90  # Start by going up
        self.create_paddle()

    def create_paddle(self):
        starting_positions = [(380, 0), (380, -20), (380, -40)]  # vertical stack on the right
        for pos in starting_positions:
            segment = Turtle("square")
            segment.color("white")
            segment.shapesize(1, 1)
            segment.penup()
            segment.goto(pos)
            self.segments.append(segment)

    def move(self):
        for segment in self.segments:
            new_y = segment.ycor() + MOVE_DISTANCE if self.direction == 90 else segment.ycor() - MOVE_DISTANCE
            segment.goto(segment.xcor(), new_y)

        # Check top or bottom boundary using the top segment
        head_y = self.segments[0].ycor()
        head_x=self.segments[0].xcor()
        if head_y >= TOP_LIMIT:
            self.direction = 270  # Down
        elif self.segments[-1].ycor() <= BOTTOM_LIMIT:
            self.direction = 90  # Up


