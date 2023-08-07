from turtle import Turtle, Screen


timmy = Turtle()
screen = Screen()


def forward():
    timmy.forward(100)
def backward():
    timmy.backward(100)

def circle():
    timmy.circle(15, 180)
def counter_cw():
    timmy.setheading(timmy.heading() + 10)
def cw():
    timmy.setheading(timmy.heading() - 10)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

# initiate event listener
screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=counter_cw)
screen.onkey(key="d", fun=cw)
screen.onkey(key="c", fun=clear)
screen.onkey(key="z", fun=circle)



screen.exitonclick()
