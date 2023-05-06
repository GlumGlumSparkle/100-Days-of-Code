from turtle import Turtle


class Filed:
    def __init__(self):
        super().__init__()
        tim = Turtle(shape="square")
        tim.penup()
        tim.pensize(2)
        tim.speed("fastest")
        tim.color("white")
        tim.goto(0, -300)
        tim.setheading(90)
        tim.hideturtle()

        for x in range(60):
            tim.pendown()
            tim.forward(10)
            tim.penup()
            tim.forward(10)
