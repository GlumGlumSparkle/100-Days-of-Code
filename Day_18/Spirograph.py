import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)
tim.speed(40)
screen = Screen()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

for _ in range (100):
    tim.circle(100)
    tim.heading()
    tim.pencolor(random_color())
    tim.left(10)

screen.exitonclick()

