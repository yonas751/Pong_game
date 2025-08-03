from turtle import Turtle,Screen
from border import Border
from paddle import Paddle
from another_paddle import AnotherPaddle
from pong import Pong
from score import Scoreboard
import time
scoreboard = Scoreboard()
screen = Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")


is_true=True
border = Border()
paddle = Paddle()
pong = Pong()
screen.listen()
screen.onkey(paddle.down, "Down")
screen.onkey(paddle.up, "Up")
another_paddle = AnotherPaddle()

while is_true:
    screen.update()
    time.sleep(0.1)
    another_paddle.move()
    pong.move()
    # Paddle contact — bounce down and reverse direction
    for segment in paddle.segments:
        if pong.distance(segment) < 30 and pong.ycor() < segment.ycor():
            pong.bounce_down()
            pong.change_direction()

    for segment in another_paddle.segments:
        if pong.distance(segment) < 30 and pong.ycor() < segment.ycor():
            pong.bounce_down()
            pong.change_direction()

        if pong.ycor() < -280:
            pong.bounce_up()
        if pong.ycor() > 280:
            if pong.x_move < 0:
                scoreboard.point_right()  # Player 2 scores
            else:
                scoreboard.point_left()  # Player 1 scores
            pong.reset_position()

screen.exitonclick()









