import datetime
import time
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
SESSION_NUMBER = 0 # includes breaks
timer = None # create global timer to be able to stop the timer

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    # stop timer
    global  timer
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text_id, text="00:00")

    # erase all checkmarks
    checkmark.config(text="")

    # reset title to original
    timer_label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))

    # reset number of sessions to zero again
    global SESSION_NUMBER
    SESSION_NUMBER = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro app")
window.config(padx=100, pady=50, bg=YELLOW)

# create timer Label at the top
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

def start_timer():

    global SESSION_NUMBER

    # update session number
    SESSION_NUMBER += 1

    # work session
    work_sec = WORK_MIN * 60

    # short break
    short_break = SHORT_BREAK_MIN * 60

    # long break
    long_break = LONG_BREAK_MIN * 60

    if SESSION_NUMBER % 2 == 0:
        if SESSION_NUMBER % 8 == 0:  # every 8th session should be a long break
            count_down(long_break)
            print(f"starting session {SESSION_NUMBER}: {LONG_BREAK_MIN}")
            timer_label.config(text="Long break", fg=RED)

        else:
            # if it's not an 8th session and is even, it's a short break
            count_down(short_break)
            print(f"starting session {SESSION_NUMBER}: {SHORT_BREAK_MIN}")
            timer_label.config(text="Short break", fg=PINK)
    else:
        # if it's odd, that means it is a work session
        count_down(work_sec)
        print(f"starting session {SESSION_NUMBER}: {WORK_MIN}")
        timer_label.config(text="Focusing", fg=PINK)

    work_session = math.floor(SESSION_NUMBER/2)
    checkmarks = ""
    for _ in range(work_session):
        checkmarks += "✔️"

    checkmark.config(text=f"{checkmarks}")


def count_down(pomodoro_duration):
    """Update timer after every second and display on pomodoro canvas.

    args:
        pomodoro_duration: time in seconds for the session.
    """
    count_min = math.floor(pomodoro_duration / 60)
    count_sec = pomodoro_duration % 60

    if count_min < 10:
        count_min = "0" + str(count_min) # prepend a zero on minutes if less than 10

    if count_sec < 10:
        count_sec = "0" + str(count_sec) # prepend a zero on seconds if less than 10

    # update timer on canvas after each second
    canvas.itemconfig(canvas_text_id, text=f"{count_min}:{count_sec}")

    if pomodoro_duration > 0:
        # keep track of the timer and update after 1000 milliseconds (1 second)
        global timer
        timer = window.after(1000, count_down, pomodoro_duration - 1)
    else:
        # automatically run timer again for next session
        start_timer()


# create start and reset buttons
start_button = Button(text="Start", bg=PINK, command=start_timer)
start_button.grid(column=0, row=2)


reset_button = Button(text="Reset", bg=PINK, command=reset_timer)
reset_button.grid(column=2, row=2)


# create canvas to lay the picture on
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

# create text to display time
canvas_text_id = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# add checkmark to count number of pomodoro sessions done
checkmark = Label(text="", fg=PINK, bg=YELLOW)
checkmark.grid(column=1, row=3)


# TODO #1: Update checkmarks after each pomodoro session to track the number
# TODO #2: work on the reset session button
# TODO #3: Allow user to choose number of sessions (maybe later)
# TODO #4: Add ringtone when time is off


window.mainloop()
