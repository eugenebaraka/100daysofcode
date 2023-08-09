from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Le Jeu de Pong")
screen.tracer(0)

positions = [(350, 0), (350, 20), (350, -20), (350, 40), (350, -40)]


paddle = Turtle("square")

paddle.color("white")
paddle.shapesize(stretch_len=1, stretch_wid=5)
paddle.penup()
paddle.setposition((350, 0))


def move_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def move_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()
