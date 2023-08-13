from turtle import Turtle

FONT = ("Courier", 20, "normal")
INITIAL_POSITION = (0, -280)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 270)
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level {self.score}", align="center", font=FONT)

    def add_point(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.reset() # move message to center
        self.write(f"GAME OVER!!\n Level {self.score}", align="center", font=FONT)
