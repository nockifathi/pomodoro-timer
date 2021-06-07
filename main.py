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
reps = 0
check = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global check, reps
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check = ""
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, check
    reps += 1
    work_time_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 1 or reps % 2 != 0:
        time = work_time_sec
        title_label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        time = long_break_sec
        title_label.config(text="Break", fg=RED)
    else:
        time = short_break_sec
        title_label.config(text="Break", fg=PINK)
    count_down(time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global check
    minutes = int(math.floor(count / 60))
    if len(str(minutes)) < 2:
        minutes = "0" + str(minutes)
    seconds = count % 60
    if len(str(seconds)) < 2:
        seconds = "0" + str(seconds)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check += "✔"
            check_mark.config(text=check)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)
title_label = Label(text="Timer", font=(FONT_NAME, 48, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)
start_btn = Button(text="Start", command=start_timer)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(column=2, row=2)
check_mark = Label(text=check, font=(FONT_NAME, 18, "bold"),bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)







window.mainloop()