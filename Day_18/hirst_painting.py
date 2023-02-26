import turtle as t
from turtle import Screen
import random

screen = Screen()
screen.colormode(255)
tim = t.Turtle()
color_list = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49),
              (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104),
              (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67),
              (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31),
              (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78),
              (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187),
              (169, 206, 172), (219, 182, 169)]

tim.hideturtle()
y = -200
tim.penup()
tim.setposition(-240, y)
tim.pendown()


def random_color():
    for x in range(len(color_list)):
        return random.choice(color_list)


def action_forward():
    for _ in range(10):
        tim.speed(30)
        tim.dot(30, random_color())
        tim.begin_fill()
        tim.penup()
        tim.forward(50)
        tim.pendown()
        tim.end_fill()


def flip(y):
    tim.penup()
    tim.setposition(-240, y)
    tim.pendown()


for _ in range(10):
    action_forward()
    y += 50
    flip(y)

screen = Screen()
screen.exitonclick()
