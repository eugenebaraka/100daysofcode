import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

#--------------------- REVEAL FRONT (QUESTION)------------------------

#--------------------- REVEAL BACK (ANSWER)------------------------
def reveal_answer(answer, text_id, image_id):
    # update image to back image
    canvas.itemconfig(image_id, image=back_img)
    # update word meaning in english
    canvas.itemconfig(text_id, text=f"English\n\n{answer}",
                             fill="red", font=("Courier", 55, "bold"), justify="center")

#--------------------- UI SET UP-------------------------
window = Tk()
window.title("Flashy Flash Cards")
window.config(bg=BACKGROUND_COLOR)

# Canvas set up
canvas = Canvas(width=800, height=650, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
image_id = canvas.create_image(412, 330, image=front_img)
canvas.grid(column=0, columnspan=3, row=1)

canvas.create_text(380, 250, text=f"Click start below to begin learning", fill="red",
                   font=("Courier", 20, "bold"))

def asks_question():
    data = pandas.read_csv("./data/french_words.csv")
    print(data.shape)
    n_qst = data.shape[0]  # number of questions

    random_qst = random.randint(0, n_qst-1)
    french = data.iloc[random_qst].French
    english = data.iloc[random_qst].English

    # front background
    image_id = canvas.create_image(412, 330, image=front_img)
    canvas.grid(column=0, columnspan=3, row=1)
    # fill in French word on canvas
    text_id = canvas.create_text(380, 250, text=f"French\n\n{french}",
                                 fill="red", font=("Courier", 55, "bold"), justify="center")
    canvas.after(4000, reveal_answer, english, text_id, image_id)

# reveal answer after 4 seconds
# canvas.after(4000, reveal_answer, english)

# BUTTONS
# Wrong answer
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, pady=-50, command=asks_question)
wrong_button.grid(column=0, row=2)

# Right answer
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, command=remove_word)
right_button.grid(column=2, row=2)

# Start Button
start_img = PhotoImage(file="./images/start.png")
start_button = Button(image=start_img, command = asks_question,
                      height=100, width=100, activebackground=BACKGROUND_COLOR)
start_button.flash()
start_button.grid(column=1, row=2)





window.mainloop()
