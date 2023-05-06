from turtle import Turtle, Screen
POSITION = (399, 299)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.acceleration = 0.1

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        self.acceleration *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.acceleration *= 0.9

    def ball_reset(self):
        self.goto(0, 0)
        self.acceleration = 0.1
        self.bounce_x()
