import random
import tkinter as tk
from tkinter import Canvas, PhotoImage
import pandas

BACKGROUND_COLOR = "#B1DDC6"
data_file = "../flashcard-project/data/french_words.csv"


## Develop the GUI
# window = Tk()
# window.title("Flashy Flash Cards")

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

        # Right and Wrong Buttons
        right_button = tk.Button(image=self.right_img,
                                 command=self.remove_question)
        right_button.grid(column=2, row=1)

        self.image_id = self.canvas.create_image(412, 280, image=self.front_img)
        self.canvas.grid(column=0, columnspan=3, row=0)

        self.text_id = self.canvas.create_text(380, 250, text= "",
                                          font=("Courier", 30, 'italic'), fill="black")
        wrong_button = tk.Button(image=self.wrong_img, command=self.ask_question)
        wrong_button.grid(column=0, row=1)

        self.ask_question()

    def ask_question(self):
        # ask question
        self.canvas.itemconfig(self.image_id, image=self.front_img)
        question, answer, idx = self.question_answer(self)
        self.canvas.itemconfig(self.text_id, text=f"French\n\n{question}")

        self.canvas.after(3000, self.change_img, answer)  # flip card after 3 seconds


    @staticmethod
    def question_answer(self):
        data = pandas.read_csv(data_file)
        random_idx = random.randint(0, data.shape[0])
        question = data.iloc[random_idx].French
        answer = data.iloc[random_idx].English

        return question, answer, random_idx

    def remove_question(self):
        pass

    def change_img(self, answer):
        # defining the image like this is not working
        # the object is being garbage collected before being used in the next line:
        # back_img = PhotoImage(file="../flashcard-project/images/card_back.png")

        self.canvas.itemconfig(self.image_id, image=self.back_img)
        self.canvas.itemconfig(self.text_id, text=f"English\n\n{answer}")
        self.canvas.after(3000, self.ask_question)








if __name__ == "__main__":
    make_gui = MakeGui()
    make_gui.mainloop()






