import tkinter as tk
from tkinter import Canvas, PhotoImage, Button

THEME_COLOR = "#375362"


class MakeGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(bg=THEME_COLOR, width=500, height=500)
        self.title("Quizler")
        self.canvas = Canvas(width=150, height=150, bg="white")
        self.canvas.grid(column=0, columnspan=2, row=0)

        self.question_id = self.canvas.create_text(80, 70, text="This is a test", fill="black")

        # false button
        self.false_img = PhotoImage(file="./images/false.png")
        false_butt = Button(image=self.false_img, command=self.wrong_answer)
        false_butt.grid(column=0, row=1)

        # true button
        self.true_img = PhotoImage(file="./images/true.png")
        true_button = Button(image=self.true_img, command=self.right_answer)
        true_button.grid(column=1, row=1)

    def right_answer(self):
        pass

    def wrong_answer(self):
        pass

    def add_text(self, question):
        self.canvas.itemconfig(self.question_id, text=question)


if __name__ == '__main__':
    gui = MakeGui()
    gui.mainloop()
