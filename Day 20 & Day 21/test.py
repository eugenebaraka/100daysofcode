from turtle import Turtle, Screen

tim = Turtle(shape="turtle")
screen = Screen()
screen.setup(width=600, height=600)
score = 0
tom = Turtle()
tom.penup()
# tom.goto(0, 580)
tom.write(f"The score test: {score}", move=True, align="center", font=('Arial', 15, 'normal'))


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




screen.listen()
screen.onkey(down, "Down")


screen.exitonclick()
