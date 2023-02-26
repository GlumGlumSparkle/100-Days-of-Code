from turtle import Turtle, Screen
import random
color = 0
y = -100
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race")
colors = ["red", "brown", "yellow", "blue", "purple", "orange"]
all_turtles =[]

for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[color])
    new_turtle.goto(-230, y)
    y += 40
    color += 1
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner")
            else:
                print(f"You lost!The {winning_color} turtle is the winner")
        random_position = random.randint(0, 10)
        turtle.forward(random_position)

screen.exitonclick()
