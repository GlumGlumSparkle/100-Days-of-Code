from turtle import Turtle, Screen
"""
W - Forwards
S - Backwards
A - Counter-Clockwise
D - Clockwise
C - Clear drawing
"""
tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_counter_clock():
    tim.left(5)


def clockwise():
    tim.right(5)


def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clock)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
