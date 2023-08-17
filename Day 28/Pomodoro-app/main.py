import datetime
import time
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro app")
window.config(padx=100, pady=50, bg=YELLOW)

# create timer Label at the top
timer_label = Label(text="Timer", fg=GREEN)
timer_label.grid(column=1, row=0)


def start_timer(minutes=25, seconds=0):
    """Starts the timer when start button is clicked"""

    pomodoro_duration = datetime.timedelta(minutes=minutes, seconds=seconds)
    total_seconds = pomodoro_duration.total_seconds()

    while total_seconds > 0:
        # keep track of the timer
        # timer = datetime.timedelta(seconds=total_seconds)

        # sleep the program by one second
        time.sleep(1)

        # update timer in the pomodoro
        # canvas["text"] = str(timer)
        canvas.itemconfig(text_id, text="i am updated")
        # canvas.grid(column=1, row=1)
        # reduce the total seconds by one second
        total_seconds -= 1


# create start and reset buttons
start_button = Button(text="Start", bg=PINK, command=start_timer)
start_button.grid(column=0, row=2)


def reset_timer():
    pass


reset_button = Button(text="Reset", bg=PINK, command=reset_timer)
reset_button.grid(column=2, row=2)


# create canvas to lay the picture on
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

# create text to display time
text_id = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# add checkmark to count number of pomodoro sessions done
checkmark = Label(text="✔", fg=PINK)
checkmark.grid(column=1, row=3)





window.mainloop()