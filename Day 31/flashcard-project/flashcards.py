import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# BACK_IMG = PhotoImage(file="./images/card_back.png")

class FlashCards:
    def __init__(self, canvas):
        window = Tk()
        window.title()
        window.config(bg=BACKGROUND_COLOR)
        self.canvas = canvas
        window.mainloop()

    # def add_front_images(self):
    #     front_img = PhotoImage(file="./images/card_front.png")
    #     self.canvas.create_image(412, 330, image=front_img)
    #     self.canvas.grid(column=0, columnspan=3, row=1)


