from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN =0.2
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps = 0
check = '✓'
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer', fg=GREEN)
    checkmarks.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    global timer_label
    reps += 1
    if reps % 8 == 0:
        countdown_time = LONG_BREAK_MIN
        text = 'Break'
        colour = RED
    elif reps % 2 == 0:
        countdown_time = SHORT_BREAK_MIN
        text = 'Break'
        colour = PINK
    else:
        countdown_time = WORK_MIN
        text = 'Work'
        colour = GREEN
    timer_label['text'] = text
    timer_label['fg'] = colour
    # another option
    # timer_label.config(text=text, fg=colour)
    count_down(countdown_time * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    minutes = int(math.floor(count/60))
    seconds = int(count % 60)
    # can use the below code to implement a switch statement so the numbers will adjust accordingly or
    # use the implemented code to save lines of code and make it a little easier to read
    # dynamic_numbers = {
    #     0: '00',
    #     1: '01',
    #     2: '02',
    #     3: '03',
    #     4: '04',
    #     5: '05',
    #     6: '06',
    #     7: '07',
    #     8: '08',
    #     9: '09'
    # }
    # if minutes < 10:
    #     minutes = dynamic_numbers[minutes]
    # if seconds < 10:
    #     seconds = dynamic_numbers[seconds]
    if minutes < 10:
        minutes = f'0{minutes}'

    if seconds < 10:
        seconds = f'0{seconds}'

    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        checkmarks.config(text=math.floor(reps / 2) * check)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 60))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text='Start', bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmarks = Label(text="", fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)


window.mainloop()
