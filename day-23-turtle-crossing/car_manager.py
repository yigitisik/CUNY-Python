import random
from turtle import Turtle

COLORS = ["red", "orange", "black", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_LINE_X, TOP_LINE_Y = 280, 250
ENDING_LINE_X, BOTTOM_LINE_Y = -280, -250

class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT

    def make_car(self):
        car_generation_freq = random.randint(1, 5)
        if car_generation_freq == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.goto(STARTING_LINE_X, random.randrange(BOTTOM_LINE_Y,TOP_LINE_Y))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.fd(self.car_speed)

    def car_increase_level_speed(self):
        self.car_speed += MOVE_INCREMENT

