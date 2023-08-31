import tkinter as tk
from tkinter import Canvas, PhotoImage, Button
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.config(bg=THEME_COLOR)
        self.window.title("Quizler")
        self.canvas = Canvas(width=500, height=500, bg="white")
        self.canvas.grid(column=0, columnspan=2, row=0, padx=15, pady=15)

        self.question_id = self.canvas.create_text(250, 250, width=480, text="This is a test",
                                                   fill="black", justify=tk.CENTER, font=("Courier", 25, "bold"))

        self.score_id = self.canvas.create_text(470, 30, text=f"Score: {self.quiz.score}/{self.quiz.question_number}",
                                                fill="black", font=("Times", 13, "italic bold"))
        # false button
        false_img = PhotoImage(file="./images/false.png")
        self.false_butt = Button(image=false_img, command=self.false_pressed, highlightthickness=0)
        self.false_butt.grid(column=0, row=1)

        # true button
        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, command=self.true_pressed, highlightthickness=0)
        self.true_button.grid(column=1, row=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_id, text=q_text)
            self.canvas.itemconfig(self.score_id,
                                   text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        else:
            self.canvas.delete(self.score_id)
            self.canvas.itemconfig(self.question_id, text=f"You've completed the quiz\n"
                                                          f"Final Score: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_butt.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")

        self.canvas.after(1000, self.get_next_question)





# class MakeGui(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.config(bg=THEME_COLOR, width=1000, height=1000)
#         self.title("Quizler")
#         self.canvas = Canvas(width=500, height=500, bg="white")
#         self.canvas.grid(column=0, columnspan=2, row=0, padx=15, pady=15)
#
#         self.question_id = self.canvas.create_text(250, 250, text="This is a test",
#                                                    fill="black", justify=tk.CENTER, font=("Courier", 25, "bold"))
#
#         # false button
#         self.false_img = PhotoImage(file="./images/false.png")
#         false_butt = Button(image=self.false_img, command=self.wrong_answer)
#         false_butt.grid(column=0, row=1)
#
#         # true button
#         self.true_img = PhotoImage(file="./images/true.png")
#         true_button = Button(image=self.true_img, command=self.right_answer)
#         true_button.grid(column=1, row=1)
#
#         self.bind("<Configure>", self.resize)
#
#     def right_answer(self):
#         pass
#
#     def wrong_answer(self):
#         pass
#
#     def add_text(self, question):
#         self.canvas.itemconfig(self.question_id, text=question)
#
#     def resize(self, event):
#         font = "Times %i italic bold"
#         fontsize = 15
#         x0 = self.canvas.bbox(self.question_id)[0]  # x-coordinate of the left side of the text
#         self.canvas.itemconfigure(self.question_id, width=self.winfo_width() - x0, font=font % fontsize)
#         # shrink to fit
#         height = self.winfo_height()  # canvas height
#         y1 = self.canvas.bbox(self.question_id)[3]  # y-coordinate of the bottom of the text
#
#         while y1 > height and fontsize > 1:
#             fontsize -= 1
#             self.canvas.itemconfigure(self.question_id, font=font % fontsize)
#             y1 = self.canvas.bbox(self.question_id)[3]
#
#
# if __name__ == '__main__':
#     gui = MakeGui()
#     gui.mainloop()
