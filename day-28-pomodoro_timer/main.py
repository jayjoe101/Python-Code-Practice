from tkinter import *
import math


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1 # constants should only be all caps
clock = None # constants should only be all caps

def reset():
    global reps
    global clock
    canvas.itemconfig(timer_text, text='00:00')
    reps = 1
    check_mark.config(text='')
    time_label.config(text='Timer', fg=GREEN)
    screen.after_cancel(clock)

def start():
    global reps
    if reps % 8 == 0:
        reps += 1
        time_label['text'] = 'Break'
        time_label['fg'] = RED
        timer(LONG_BREAK_MIN )
    elif reps % 2 == 0:
        reps += 1
        time_label['text'] = 'Break'
        time_label['fg'] = PINK
        timer(SHORT_BREAK_MIN )
    else:
        reps += 1
        time_label['text'] = 'Work'
        time_label['fg'] = GREEN
        timer(WORK_MIN )


def timer(count):
    """input desired minutes"""
    s = math.floor(count % 60)
    m = math.floor((count / 60) % 60)
    canvas.itemconfig(timer_text, text=f'{int(m):02d}:{int(s):02d}')
    if count > 0:
        global clock
        clock = screen.after(1000, timer, count - 1)
    else:
        if reps % 2 == 0:
            check_mark['text'] += '✔'
        start()


screen = Tk()
screen.title('Pomodoro')
screen.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png') 
canvas.create_image(100, 112, image=tomato_img) # this doesnt like specifying width and height and needs a photoimage object instead of str for the file location
# divide half of the canvas width and height to center items
timer_text = canvas.create_text(100, 135, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

canvas.grid(row=1, column=1)

time_label = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 45, 'bold'), bg=YELLOW)
start_button = Button(text='Start',highlightthickness=0, command = start)
reset_button = Button(text='Reset',highlightthickness=0, command = reset)
check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, 'bold'))

time_label.grid(row=0, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
check_mark.grid(row=3, column=1)


screen.mainloop()