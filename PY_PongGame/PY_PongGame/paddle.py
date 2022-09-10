from turtle import Turtle

COLOR = "white"
WIDTH_MULTIPLY = 1
HEIGHT_MULTIPLY = 5
SHAPE = "square"
HEADING = 90 
MOVE_RANGE = 20

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.shapesize(stretch_wid = WIDTH_MULTIPLY, stretch_len = HEIGHT_MULTIPLY)
        self.goto(coordinates)
        self.setheading(HEADING)

    def move_up(self)->None:
        """Moves paddle up
        """
        self.forward(MOVE_RANGE)

    def move_down(self)->None:
        """moves paddle down
        """
        self.backward(MOVE_RANGE)
