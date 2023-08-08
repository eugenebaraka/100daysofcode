from turtle import Turtle, Screen

tim = Turtle(shape="turtle")

def up():
    tim.setheading(90)
    tim.forward(10)

def down():
    tim.setheading(270)
    tim.forward(10)

def left():
    tim.setheading(180)
    tim.forward(10)

def right():
    tim.setheading(360)
    tim.forward(10)



screen = Screen()
screen.listen()
screen.onkey(down, "Down")


screen.exitonclick()
