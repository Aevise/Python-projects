from turtle import Turtle
from random import randint

COLOR = "pink"
SHAPE = "circle"

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(COLOR)
        self.speed("fastest")
        self.place_new_food()

    
    def place_new_food(self)->None:
        """places the food on the random position on the screen.
        """
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y) 
