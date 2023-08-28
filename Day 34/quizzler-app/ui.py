import tkinter as tk
from tkinter import Canvas, PhotoImage, Button

THEME_COLOR = "#375362"


class MakeGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(bg=THEME_COLOR, width=1000, height=1000)
        self.title("Quizler")
        self.canvas = Canvas(width=500, height=500, bg="white")
        self.canvas.grid(column=0, columnspan=2, row=0, padx=15, pady=15)

        self.question_id = self.canvas.create_text(250, 250, text="This is a test",
                                                   fill="black", justify=tk.CENTER, font=("Courier", 25, "bold"))

        # false button
        self.false_img = PhotoImage(file="./images/false.png")
        false_butt = Button(image=self.false_img, command=self.wrong_answer)
        false_butt.grid(column=0, row=1)

        # true button
        self.true_img = PhotoImage(file="./images/true.png")
        true_button = Button(image=self.true_img, command=self.right_answer)
        true_button.grid(column=1, row=1)

        self.bind("<Configure>", self.resize)

    def right_answer(self):
        pass

    def wrong_answer(self):
        pass

    def add_text(self, question):
        self.canvas.itemconfig(self.question_id, text=question)

    def resize(self, event):
        font = "Times %i italic bold"
        fontsize = 15
        x0 = self.canvas.bbox(self.question_id)[0]  # x-coordinate of the left side of the text
        self.canvas.itemconfigure(self.question_id, width=self.winfo_width() - x0, font=font % fontsize)
        # shrink to fit
        height = self.winfo_height()  # canvas height
        y1 = self.canvas.bbox(self.question_id)[3]  # y-coordinate of the bottom of the text

        while y1 > height and fontsize > 1:
            fontsize -= 1
            self.canvas.itemconfigure(self.question_id, font=font % fontsize)
            y1 = self.canvas.bbox(self.question_id)[3]


if __name__ == '__main__':
    gui = MakeGui()
    gui.mainloop()
