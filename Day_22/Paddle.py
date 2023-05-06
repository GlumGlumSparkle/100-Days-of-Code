from turtle import Turtle

STARTING_POSITION_PADDLE1 = (350, 0)
STARTING_POSITION_PADDLE2 = (-350, 0)


class Paddle1(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(STARTING_POSITION_PADDLE1)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


class Paddle2(Paddle1):
    def __init__(self):
        super().__init__()
        self.goto(STARTING_POSITION_PADDLE2)
