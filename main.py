import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
game_is_on = True
screen.listen()
screen.onkey(player.dodge, "space")
car_manager = CarManager()
scoreboard = Scoreboard()
score = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.make_car()
    car_manager.move_it()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.finished():
        car_manager.speed_up()
        player.go_to_start()
        scoreboard.nxt_lvl()

screen.exitonclick()
