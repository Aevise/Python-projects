from turtle import Turtle
from random import choice

COLOR = "white"
SHAPE = "circle"
MOVE_RANGE = 20
HEADING = [45, 135, 225, 315]
SPEED_INCREASE = 0.9
DEFAULT_MOVEMENT = 10
DEFAULT_SPEED = 0.1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)        
        self.penup()
        self.x_move = DEFAULT_MOVEMENT
        self.y_move = DEFAULT_MOVEMENT
        self.move_speed = DEFAULT_SPEED
        self.setheading(choice(HEADING))

    def move_ball(self)->None:
        """constantly moves ball forward
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self)->None:
        """Makes ball move up or down
        """
        self.y_move *= -1

    def bounce_x(self)->None:
        """Make ball move left or right
        """
        self.x_move *= -1

    def reset_position(self)->None:
        """Resets ball's position and then sets it's heading to random
        """
        self.setposition(0, 0)
        self.setheading(choice(HEADING))
        self.reset_ball_speed()

    def increase_ball_speed(self)->None:
        """Increases the speed of the ball
        """
        self.move_speed *= SPEED_INCREASE
    
    def reset_ball_speed(self)->None:
        """Resets ball speed to default value
        """
        self.move_speed = 0.1