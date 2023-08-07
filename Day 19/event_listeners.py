from turtle import Turtle, Screen

# Event listeners
timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward) # higher order function: function that can work with other functions
screen.exitonclick()
