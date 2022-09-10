from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
SHAPE = "turtle"
COLOR = "black"

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.color(COLOR)
        self.setheading(90)
        self.starting_position()

    def move_forward(self)->None:
        """Moves player forward 
        """
        self.forward(MOVE_DISTANCE)

    def starting_position(self)->None:
        """Sets a player to the starting position
        """
        self.setposition(STARTING_POSITION)