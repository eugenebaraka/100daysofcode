from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("square")
timmy.color("blue")

for _ in range(4):
    timmy.forward(100)
    timmy.left(90)


screen = Screen()
screen.exitonclick()
