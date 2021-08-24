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
LONG_BREAK_MIN = 20
CHECK_MARK = "✓"

# ---------------------------- GLOBAL VARIABLES ------------------------------- #
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_time_in_seconds = WORK_MIN * 60
    short_break_in_seconds = SHORT_BREAK_MIN * 60
    long_break_in_seconds = LONG_BREAK_MIN * 60

    rep_modulo = reps % 8
    if rep_modulo % 2 == 1:
        # Work Time
        count_down_time_in_seconds = work_time_in_seconds
        title_label.config(text="Work", fg=GREEN)
    elif rep_modulo == 0:
        # Long Break
        count_down_time_in_seconds = long_break_in_seconds
        title_label.config(text="Break", fg=RED)
    else:
        count_down_time_in_seconds = short_break_in_seconds
        title_label.config(text="Break", fg=PINK)
    count_down(count_down_time_in_seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes_left = math.floor(count / 60)
    seconds_left = count % 60
    if seconds_left < 10:
        seconds_left = f"0{seconds_left}"
        # Python is strongly typed, but also has Dynamic Typing
        # Strongly typed - Strong typing means that the type of a value doesn't change in unexpected ways. A string
        #   containing only digits doesn't magically become a number, as may happen in Perl. Every change of type
        #   requires an explicit conversion.Each variable has a type and it remembers its type. If you do an operation
        #   which is not supported on the type, you will get a 'TypeError'. e.g. trying to do ** (power) operation
        #   on a string.
        # Dynamic Typing - Dynamic typing means that runtime objects (values) have a type, as opposed to static typing
        #   where variables have a type. In python, you are allowed to change the type of a variable. e.g. here we are
        #   changing the type of 'seconds_left' variable from int to str.
    canvas.itemconfig(timer_text, text=f"{minutes_left}:{seconds_left}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_marks_text = ""
        num_check_marks = math.floor(reps / 2)
        for i in range(num_check_marks):
            check_marks_text += CHECK_MARK
        check_marks_label.config(text=check_marks_text)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # same as tomato.png
canvas.create_image(100, 112, image=tomato_image)  # half of above
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightbackground=YELLOW, foreground=RED, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightbackground=YELLOW, foreground=RED, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks_label = Label(font=(FONT_NAME, 25), fg=GREEN, bg=YELLOW)
check_marks_label.grid(row=3, column=1)

window.mainloop()
