import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=600)
screen.title("Turtle Car Crossing")
screen.tracer(0) # to prevent animation when building cars

player = Player()
cars = CarManager()
score = ScoreBoard()


screen.listen()
screen.onkey(player.move_up, "Up")


game_is_on = True

while game_is_on:

    screen.update()
    cars.generate_car()
    time.sleep(0.1)
    cars.move_cars()

    # detect a successful crossing
    if player.is_at_finishline():
        score.add_point()
        player.reset_player() # reset player position
        cars.level_up() # increase the speed of cars

    # detect collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()








screen.exitonclick()



