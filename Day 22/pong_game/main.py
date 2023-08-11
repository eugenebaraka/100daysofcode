import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Le Jeu de Pong")
screen.tracer(0)


LEFT_POS = (-350, 0)
RIGHT_POS = (350, 0)
ball = Ball()

left_paddle = Paddle(LEFT_POS)
right_paddle = Paddle(RIGHT_POS)

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "a")
screen.onkey(left_paddle.move_down, "z")

game_is_on = True


def collision():
    if ball.ycor() > 200:
        x = ball.xcor() * 2
        y = 0
        ball.goto(x, y)
        
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()




screen.exitonclick()
