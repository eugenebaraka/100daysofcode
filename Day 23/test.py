import time
from turtle import Turtle, Screen
import random

colors = ["green", "yellow", "blue", "orange", "purple", "pink",
          "royal blue", "lime green", "dark khaki", "linen", "medium orchid"]

STARTING_POSITION = (0, -280)

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)


for _ in range(len(colors)):
    time.sleep(0.01)
    screen.update()
    t = Turtle("square")
    t.penup()
    t.color(random.choice(colors))
    t.turtlesize(stretch_wid=1, stretch_len=2)
    t.goto(random.randint(-300, 300), random.randint(-300, 300))

screen.exitonclick()
