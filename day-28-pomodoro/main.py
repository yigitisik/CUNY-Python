 import math
from tkinter import *
#to make clickable app work:
import os, sys
def resource_path(relative_path):
    """ Get absolute path to resource, works for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Example usage:
my_image = resource_path("do it.png")
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ("Courier", 24, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer Reset", fg=PINK)
    canvas.itemconfig(timer_text, text="00:00")
    cycle_count.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    work_secs = WORK_MIN*60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_secs)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_secs)
        timer_label.config(text="Focus Time", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import time
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    #dynamic type we display 5:00 instead of 5:0
    if count_sec < 10:
        count_sec = "0"+str(count_sec) # or do f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        cycle_count.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPomodoro")
window.config(padx=50,pady=50, bg=YELLOW)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2,column=2)

timer_label = Label(text="Timer", font=FONT, fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

cycle_count = Label(fg=GREEN, bg=YELLOW)
cycle_count.grid(row=3, column=1)

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
image_path = PhotoImage(file=resource_path("do it.png"))
canvas.create_image(100, 112, image=image_path)
timer_text = canvas.create_text(100,130, text="00:00", font=FONT, fill="white")
canvas.grid(row=1,column=1)


window.mainloop()
