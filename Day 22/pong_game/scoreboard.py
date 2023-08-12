from turtle import Turtle

L_SCORE_POS = (-100, 200)
R_SCORE_POS = (100, 200)
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(L_SCORE_POS)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(R_SCORE_POS)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
