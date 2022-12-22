from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance_cars = random.randint(1, 6)
        if chance_cars == 6:
            cars = Turtle("square")
            cars.shapesize(stretch_len=1, stretch_wid=0.5)
            cars.penup()
            cars.color(random.choice(COLORS))

            # genrating random cars
            random_y = random.randint(-250,250)
            cars.goto(300, random_y)
            self.all_cars.append(cars)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
