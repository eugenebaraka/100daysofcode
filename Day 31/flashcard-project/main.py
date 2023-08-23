import random
import tkinter as tk
from tkinter import Canvas, PhotoImage
import pandas

BACKGROUND_COLOR = "#B1DDC6"
data_file_read_only = "./data/french_words.csv"
data_file = "./data/practice.csv"


class MakeGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(bg=BACKGROUND_COLOR)
        self.title("Flashy Flash Cards")
        self.canvas = Canvas(width=800, height=535,
                             bg=BACKGROUND_COLOR, highlightthickness=0) # to overlay pictures and text

        self.front_img = PhotoImage(file="../flashcard-project/images/card_front.png")
        self.back_img = PhotoImage(file="../flashcard-project/images/card_back.png")
        self.wrong_img = PhotoImage(file="../flashcard-project/images/wrong.png")
        self.right_img = PhotoImage(file="../flashcard-project/images/right.png")

        self.image_id = self.canvas.create_image(412, 280, image=self.front_img)
        self.canvas.grid(column=0, columnspan=3, row=0)

        self.text_id = self.canvas.create_text(380, 250, text= "",
                                          font=("Courier", 30, 'italic'), fill="black")

        wrong_button = tk.Button(image=self.wrong_img, command=self.ask_question)
        wrong_button.grid(column=0, row=1)

        self.right_button = tk.Button(image=self.right_img)
        self.right_button.grid(column=2, row=1)

        try:
            self.data = pandas.read_csv(data_file)
        except FileNotFoundError:
            self.data = pandas.read_csv(data_file_read_only)

        self.ask_question()

    def ask_question(self):

        self.canvas.itemconfig(self.image_id, image=self.front_img)
        question, answer, idx = self.question_answer(self)
        self.canvas.itemconfig(self.text_id, text=f"French\n\n{question}")

        self.canvas.after(3000, lambda: self.change_img(answer, idx))

    @staticmethod
    def question_answer(self):
        # random_idx = random.randint(0, self.data.shape[0])
        print(self.data.index)
        random_idx = random.choice(self.data.index)
        print(random_idx)
        question = self.data.iloc[random_idx].French
        answer = self.data.iloc[random_idx].English

        return question, answer, random_idx

    @staticmethod
    def remove_question(self, idx):
        self.data.drop(index = idx, inplace=True)
        self.data.to_csv(data_file, index=False)
        self.ask_question()

    def change_img(self, answer, idx):
        self.canvas.itemconfig(self.image_id, image=self.back_img)
        self.canvas.itemconfig(self.text_id, text=f"English\n\n{answer}")

        # evaluate whether wrong or right, if right remove question
        self.right_button.config(command = lambda: self.remove_question(self, idx))

if __name__ == "__main__":
    make_gui = MakeGui()
    make_gui.mainloop()
