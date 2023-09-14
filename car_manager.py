from random import *
from turtle import *

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def make_car(self):
        if randint(1, 6) == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-240, 250)
            new_car.goto(300, random_y)
            new_car.rt(180)
            self.all_cars.append(new_car)

    def move_it(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT

        pass


"""        self.col=choice(COLORS)
        self.color(self.col)
        self.penup()
        self.goto(280, randint(-240, 250))
        self.shape("square")
        self.shapesize(stretch_len=3)
        self.rt(180)
"""
