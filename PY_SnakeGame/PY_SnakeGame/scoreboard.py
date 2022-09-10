from ctypes import alignment
from turtle import Turtle
import os.path

COLOR = "white"
END_COLOR = "red"
ALIGN = "center"
FONT = ("Arial", 14, "normal")
SCOREBOARD_FILE = "scoreboard.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.initialize_score_file()
        self.score = 0
        self.hideturtle()
        self.color(COLOR)
        self.penup()
        self.goto(0, 280)
        self.refresh()
        
    def initialize_score_file(self)->None:
        """checks if score file exists
        If not, creates a new file with starting value 0
        """
        if(os.path.exists(SCOREBOARD_FILE) == False):
            with open(file = SCOREBOARD_FILE, mode = "w") as file:
                file.write(str(self.high_score))
        else:
            with open(file = SCOREBOARD_FILE, mode = "r") as file:
                self.high_score = file.read()

    def save_score(self):
        with open(file = SCOREBOARD_FILE, mode = "w") as file:
            file.write(str(self.high_score))

    def add_score(self)->None:
        """Adds one point and refreshes scoreboard
        """
        self.score += 1
        self.refresh()

    def hit_wall(self)->None:
        """Generates Game Over message when snake hits wall
        """
        self.goto(0,0)
        self.color(END_COLOR)
        self.write(arg = "     GAME OVER.\nYou have hit the wall.", align=ALIGN, font=FONT)
        self.goto(0, -50)
        self.write(arg = "Game will reset in 5 seconds", align=ALIGN, font=FONT)
        

    def hit_tail(self)->None:
        """Generates game over message when snake hits its tails
        """
        self.goto(0,0)
        self.color(END_COLOR)
        self.write(arg = "     GAME OVER.\nYou have hit your tail.", align=ALIGN, font=FONT)
        self.goto(0, -50)
        self.write(arg = "Game will reset in 5 seconds", align=ALIGN, font=FONT)

    def refresh(self)->None:
        """Refresh scoreboard and writes a new value.
        """
        self.clear()
        self.goto(0, 280)
        self.color(COLOR)
        self.write(arg = f"Score: {self.score}. High score: {self.high_score}", align=ALIGN, font=FONT)

    def highest_score(self):
        if int(self.high_score) < self.score:
            self.high_score = self.score  
            self.save_score()  
        self.score = 0