import time
from turtle import Screen
from Play_Filed import Filed
from Scoreboard import Scoreboard
from Paddle import Paddle1, Paddle2
from Ball import Ball

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
filed = Filed()
scorebard = Scoreboard()
r_paddle = Paddle1()
l_paddle = Paddle2()
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, key="Up")
screen.onkey(r_paddle.go_down, key="Down")
screen.onkey(l_paddle.go_up, key="d")
screen.onkey(l_paddle.go_down, key="x")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.acceleration)
    ball.ball_move()
    # detect the collition with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        screen.tracer(2)
        ball.bounce()

    # detect collition with a right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or \
            ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()

    # Score to left paddle
    if ball.xcor() > 395:
        scorebard.l_point()
        ball.ball_reset()

    # Score to right paddle
    if ball.xcor() < -395:
        ball.ball_reset()

screen.exitonclick()
