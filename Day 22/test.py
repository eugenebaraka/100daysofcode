from turtle import Turtle, Screen

HEIGHT = 600
WIDTH = 800
INITIAL_POS = (0, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
t = Turtle("circle")
t.color("white")
t.penup()
t.goto(INITIAL_POS)

def collision():
    if t.ycor() > HEIGHT/2 - 2:
        x = t.xcor() * 2
        y = INITIAL_POS[0]
        t.goto(x, y)




game_is_on = True

while game_is_on:
    new_x = t.xcor() + 10
    new_y = t.ycor() + 10
    t.goto(new_x, new_y)

    collision()





screen.exitonclick()
