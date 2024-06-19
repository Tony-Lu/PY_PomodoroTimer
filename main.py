
from tkinter import *
from tkinter import messagebox
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER MECHANISM ------------------------------- #
# WORK_MIN = 3
# SHORT_BREAK_MIN = 1
# LONG_BREAK_MIN = 2
# reps = 0


def start_timer():
    start_button.config(state=DISABLED)
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(fg=RED, text="Long Break")
        count_down(long_break_sec)

    elif reps % 2 == 0:
        timer_label.config(fg=PINK, text="Short Break")
        count_down(short_break_sec)

    elif reps > 8:
        messagebox.showinfo("End", "Time Cycle Completed")

    else:
        timer_label.config(fg=GREEN, text="Work")
        count_down(work_sec)


def reset_timer():
    start_button.config(state=ACTIVE)
    global reps
    reps = 0
    window.after_cancel(str(timer))
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    marks = ""
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            checkmark_label.config(text=marks)
    # mac n/a
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    window.deiconify()
    window.bell()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.config(padx=1, pady=1)
checkmark_label.grid(column=1, row=3)

timer_label = Label(text="Timer", font=(FONT_NAME, 48, "normal"), fg=GREEN, bg=YELLOW)
timer_label.config(padx=1, pady=1)
timer_label.grid(column=1, row=0)


window.mainloop()


