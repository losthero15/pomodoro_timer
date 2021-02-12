from math import floor
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "white"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#379B46"
YELLOW = "#f7f5dd"
PARANOID = "#181B28"
FONT_TIMER_CLOCK = ("Courier", 25, "bold")
FONT_LABEL = ("Helvetica", 10, "normal")
FONT_TIMER_LABEL = ("Helvetica", 25, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
level = 1
round_of_work = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, level, round_of_work
    window.after_cancel(timer)
    reps = 0
    level = 1
    round_of_work = 0
    timer_label.config(text="Pomodoro", fg=GREEN, )
    cycle_label.config(text="Get ready")
    level_label.config(text=f"Level: 0")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps, level, round_of_work
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        level += 1
        time = long_break_sec
        timer_label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        time = short_break_sec
        timer_label.config(text="Break", fg=PINK)
    else:
        round_of_work += 1
        time = work_sec
        timer_label.config(text="Work", fg=GREEN)

    cycle_label.config(text=f"Round {round_of_work}")
    level_label.config(text=f"Level: {level}")
    count_down(time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minutes = str(floor(count / 60)).zfill(2)
    seconds = str(count % 60).zfill(2)

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=20, pady=30, bg=PARANOID)

canvas = Canvas(width=200, height=224, bg=PARANOID, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill=WHITE, font=FONT_TIMER_CLOCK)
canvas.grid(row=1, column=1)

button_start = Button(text="Start", highlightthickness=0, font=FONT_LABEL, command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", highlightthickness=0, font=FONT_LABEL, command=reset_timer)
button_reset.grid(row=2, column=2)

timer_label = Label(text="Pomodoro", font=FONT_TIMER_LABEL, fg=GREEN, pady=20)
timer_label.grid(row=0, column=1)

cycle_label = Label(text="Get ready", fg=GREEN, pady=20, font=FONT_LABEL)
cycle_label.grid(row=3, column=1)

level_label = Label(text="Level: 0")
level_label.grid(row=4, column=1)

window.mainloop()
