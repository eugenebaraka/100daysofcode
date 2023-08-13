from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.setposition(0, 230)
        self.score = 0
        self.highest_score = self.read_data()
        self.update_scoreboard()
        self.hideturtle()

    @staticmethod
    def read_data():
        with open("score_data.txt", "r") as score_data:
            contents = score_data.readline()
            return int(contents)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}\nHighest Score: {self.highest_score}",
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > int(self.highest_score):
            self.highest_score = self.score
            # update the highest score file as well
            with open("score_data.txt", "w") as new_score:
                new_score.write(f"{self.highest_score}")

        self.score = 0
        self.update_scoreboard()
