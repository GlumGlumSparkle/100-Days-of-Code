import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

screen = Screen()
screen.setup(width=600, height=600)
tim.speed(10)
tim.pensize(10)
steps = [10, 20, 30, 40, 50]
angle = [0, 90, 180, 270]


def random_walk():
    for _ in range(10000):
        tim.color(random_color())
        tim.forward(random.choice(steps))
        tim.setheading(random.choice(angle))
random_walk()
