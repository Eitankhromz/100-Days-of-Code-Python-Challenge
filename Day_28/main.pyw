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
timer = None
pause = False

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    start_button.config(text="Start", state="normal", command=start_timer)
    reset_button.config(state="disabled")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", font=(FONT_NAME, 50, "normal"), bg=YELLOW, fg=GREEN, highlightthickness=0)
    check_marks_label.config(text="")
    reps = 0
    global pause
    pause = False

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    # start_button.config(state="disabled")
    reset_button.config(state="normal")

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)

    if start_button["text"] == "Start":
        start_button.config(text="Pause", command=pause_timer)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        if pause:
            timer = window.after(0, count_down, count)
        else:
            timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks_label.config(text=marks)

# ---------------------------- PAUSE/RESUME MECHANISM ------------------------------- #
def pause_timer():
    global pause #False
    pause = not pause #TRUE
    if pause: #If True or If Pause is on
        start_button.config(text="Resume")
    else: #when False
        start_button.config(text="Pause")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
# window.bell()
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "normal"), bg=YELLOW, fg=GREEN, highlightthickness=0)
timer_label.grid(column=1, row=0)

check_marks_label = Label(text="", font=(FONT_NAME, 18, "normal"), bg=YELLOW, fg=GREEN, highlightthickness=0)
check_marks_label.grid(column=1, row=3)

start_button = Button(text="Start", highlightthickness=0, command=start_timer, state="normal")
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, state="disabled")
reset_button.grid(column=2, row=2)


window.mainloop()
