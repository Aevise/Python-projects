#WOULD BE BETTER IF POMIDORRO WAS CREATED AS ANOTHER CLASS, BUT I DON'T MIND

from tkinter import *
from playsound import playsound
from math import floor

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ("Courier", 30, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REP = 1
CHECK_MARK = "✓"
WORK_PROGRESS = ""
TIMER = None
BUTTON_CLICKED = False
# ---------------------------- SOUND FILES ---------------------------- #
GONG_PATH = "/users/aevir/source/repos/PY_Pomdorro/PY_Pomdorro/GONG.mp3"
UP_PATH = "/users/aevir/source/repos/PY_Pomdorro/PY_Pomdorro/UP.mp3"

def window_on_top()->None:
    """Places a window on top of the screen
    """
    window.attributes("-topmost", True)
    if REP % 2 == 0:
        play_up()
    else:
        play_gong()
    window.attributes("-topmost", False)    

def play_gong()->None:
    """Plays a sound of a gong
    """
    playsound(GONG_PATH)

def play_up()->None:
    """Plays a sound of powering up
    """
    playsound(UP_PATH)
# ---------------------------- TIMER RESET ------------------------------- # 
def reset()->None:
    """Resets a window to it's starting configuration
    """
    global REP, TIMER, WORK_PROGRESS 
    REP = 1
    checkmark_label.config(text = "")
    window.after_cancel(TIMER)
    canvas.itemconfig(count_timer, text = "00:00")
    WORK_PROGRESS = ""
    timer_label.config(text = "Timer", fg = GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer()->None:
    """Responsible for printing out correct message and playing of a sound
    """
    global REP, WORK_PROGRESS, CHECK_MARK 

    if REP % 8 == 0:
        timer_label.config(text = "BREAK", fg = RED)
        countdown(LONG_BREAK_MIN * 60)
        WORK_PROGRESS += CHECK_MARK
        checkmark_label.config(text = WORK_PROGRESS)
    elif REP % 2 == 0:        
        timer_label.config(text = "BREAK", fg = PINK)
        countdown(SHORT_BREAK_MIN * 60)
        WORK_PROGRESS += CHECK_MARK
        checkmark_label.config(text = WORK_PROGRESS)
    else:
        timer_label.config(text = "WORK", fg = GREEN)
        countdown(WORK_MIN * 60)       
    
    window_on_top()
    REP += 1 

def click_button()->None:
    """Checks if the start button was clicked. When clicked again, start button will act just like the reset button
    """
    global BUTTON_CLICKED
    if BUTTON_CLICKED == False:
        BUTTON_CLICKED = True
        start_timer()
    else:
        BUTTON_CLICKED = False
        reset()
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(minutes:int)->None:
    """counts the remaining time of each action and displays a value in the middle of a potato

    Args:
        minutes (int): argument is self explanatory
    """
    global TIMER, REP
    count_minute = floor(minutes / 60)
    count_seconds = minutes % 60

    if count_minute < 10:
        count_minute = "0" + str(count_minute)
    if count_seconds < 10:
        count_seconds = "0" + str(count_seconds)

    canvas.itemconfig(count_timer, text = f"{count_minute}:{count_seconds}")
    if minutes >= 0:
        TIMER = window.after(1, countdown, minutes - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomdiorro")
window.config(padx = 100, pady = 50, bg = YELLOW)
window.after(1000, )

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_image)
count_timer = canvas.create_text(100, 130, text = "00:00", fill = "white", font = FONT)
canvas.grid(column = 1, row = 1)

timer_label = Label(pady = 5, text = "Timer", bg = YELLOW, fg = GREEN, font = FONT)
timer_label.grid(column = 1, row = 0)

button_start = Button(text = "Start", highlightthickness=0, command = click_button)
button_start.grid(column = 0, row = 2)

button_reset = Button(text = "Reset", highlightthickness=0, command = reset)
button_reset.grid(column = 2, row = 2)

checkmark_label = Label(bg = YELLOW, fg = GREEN)
checkmark_label.grid(column = 1, row = 3)

window.mainloop()