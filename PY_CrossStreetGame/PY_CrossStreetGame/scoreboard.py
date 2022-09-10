from turtle import Turtle

FONT = ("Arial", 20, "normal")
COLOR = "black"
END_COLOR = "red"
END_FONT = ("Arial", 30, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 265)
        self.level = 1
        self.refresh()
        self.color(COLOR)

    def next_level(self)->None:
        """Increases the number of player level
        """
        self.level += 1
        self.refresh()

    def refresh(self)->None:
        """Refreshes the screen
        """
        self.clear()
        self.write(arg = f"Level: {self.level}", font = FONT)

    def end_screen(self)->None:
        """Displays a message when you lose a game
        """
        self.goto(-125, 0)
        self.color(END_COLOR)
        self.write(arg = f"GAME OVER", font = END_FONT)
