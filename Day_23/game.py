import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkey(player.go_up, key="Up")

cars = CarManager()
scoreboard = Scoreboard()
scoreboard.level()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    cars.create_car()
    cars.car_move()
    for car_object in cars.all_cars:
        if player.distance(car_object) < 20:
            game_is_on = False
            scoreboard.game_over_text()
    if player.ycor() > 240:
        player.go_to_start()
        scoreboard.level_update()
        cars.move_increment()

    if scoreboard.level_value == 3:
        scoreboard.game_won()
        game_is_on = False











screen.exitonclick()


