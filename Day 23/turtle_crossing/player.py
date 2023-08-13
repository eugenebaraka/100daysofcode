from turtle import Turtle

INITIAL_POSITION = (0, -280)
FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_player()
        self.setheading(90)
        self.x_move = 0
        self.y_move = 0

    def move(self):
        self.goto(self.x_move, self.y_move)

    def move_up(self):
        self.y_move = self.ycor() + 10
        self.move()

    def reset_player(self):
        self.goto(INITIAL_POSITION)

    def is_at_finishline(self):
        return self.ycor() > FINISH_LINE






