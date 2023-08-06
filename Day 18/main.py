import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

colors = ["royal blue", "lime green", "dark khaki", "linen", "medium orchid"]
directions = [0, 90, 180, 270]
timmy.pensize(10)
timmy.speed("fastest")

for _ in range(600):
    timmy.color(random_color())

    timmy.forward(30)
    timmy.setheading(random.choice(directions))





screen = t.Screen()
screen.exitonclick()
