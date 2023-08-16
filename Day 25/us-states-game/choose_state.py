from turtle import Turtle

class ChooseState(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def move_answer(self, x, y, answer):
        self.write(f"{answer.capitalize()}")
        self.goto(x, y)




