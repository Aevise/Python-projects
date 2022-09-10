from turtle import Turtle

COLOR = "white"
FONT = ("Arial", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.l_paddle_score = 0
        self.r_paddle_score = 0
        self.write_score()

    def write_score(self)->None:
        """Writes current score at the top of the screen
        """
        self.clear()
        self.goto(-100,225)
        self.write(self.l_paddle_score, font = FONT)
        self.goto(100, 225)
        self.write(self.r_paddle_score, font = FONT)

    def r_score(self)->None:
        """Increment r_paddle_score by 1
        """
        self.r_paddle_score += 1
        self.write_score()

    def l_score(self)->None:
        """Increment l_paddle_score by 1
        """
        self.l_paddle_score += 1
        self.write_score()