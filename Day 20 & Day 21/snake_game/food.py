import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        # create random position of the food particle
        random_x = random.randint(-280, 260) # the screen size is -300,300
        random_y = random.randint(-280, 260)
        self.goto(random_x, random_y)



