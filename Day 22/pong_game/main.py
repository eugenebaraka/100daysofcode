import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Le Jeu de Pong")
screen.tracer(0)


LEFT_POS = (-350, 0)
RIGHT_POS = (350, 0)


left_paddle = Paddle(LEFT_POS)
right_paddle = Paddle(RIGHT_POS)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "a")
screen.onkey(left_paddle.move_down, "z")

game_is_on = True

        
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.speed("fastest")  # increase the ball speed when hit the paddle
        ball.bounce_x()

    # detect right paddle miss
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.l_point()

    # detect left paddle miss
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.r_point()









screen.exitonclick()
