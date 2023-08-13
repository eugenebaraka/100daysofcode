import random
from turtle import Turtle

COLORS = ["green", "yellow", "blue", "orange", "purple", "pink",
          "royal blue", "lime green", "dark khaki", "linen", "medium orchid"]

MOVE_DISTANCE = 10
MOVE_INCREMENT = 5

class CarManager:
    def __init__(self):
        self.all_cars= []
        self.car_speed = MOVE_DISTANCE

    def generate_car(self):
        roll_dice = random.randint(1, 6)
        if roll_dice == 6:
            new_car = Turtle("square")
            new_car.turtlesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT




        



