from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("DarkSeaGreen4")
colors = ["DarkGoldenrod1", "DarkOliveGreen", "chocolate", "coral", "bisque3"]
"""Task.1 Moving turtle to particular place on the screen"""
# tim.penup()
# tim.goto(-100, 100)
# tim.pendown()

"""Task.2 Drawing a Dashed Line"""
# for _ in range(15):
#     tim.penup()
#     tim.fd(10)
#     tim.pendown()
#     tim.fd(10)

"""Task.3 Drawing different shapes"""
# sides = 3
# for _ in range(3, 11):
#     tim.pencolor(random.choice(colors))
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(360/sides)
#     sides += 1

"""Task.4 Generate random walk"""
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
tim.speed(10)
tim.pensize(10)
steps = [10, 20, 30, 40, 50]
angle = [0, 90, 180, 270]


def random_walk():
    for _ in range(10000):
        tim.color(random.choice(colors))
        tim.forward(random.choice(steps))
        tim.setheading(random.choice(angle))

random_walk()


screen.exitonclick()
