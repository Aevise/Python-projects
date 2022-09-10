from turtle import Turtle

MOVEMENT = 20
SNAKE_COLOR = "white"
SNAKE_SHAPE = "square"
STARTING_SEGMENTS = 3
HEAD_RIGHT = 0
HEAD_UP = 90
HEAD_LEFT = 180
HEAD_DOWN = 270


class Snake():
    def __init__(self):
        self.snake_segments = self.draw_snake()
        self.head = self.snake_segments[0]
        self.tail_x = 0

    def draw_snake(self)->list:
        """
        Print a snake on a screen. Each segment of a snake is a turtle object
        shapes as a square.
        Returns lists of snake segments.
        """
        self.tail_x = 0
        new_snake = []
        for t_index in range(STARTING_SEGMENTS):
            new_snake.append(Turtle(shape=SNAKE_SHAPE))
            new_snake[t_index].color(SNAKE_COLOR)
            new_snake[t_index].penup()
            new_snake[t_index].setx(self.tail_x)
            self.tail_x -= 20
        return new_snake

    def move_snake(self)->None:
        """Moves snake forward. Snake position is updated from its tail.
        """
        for seg_index in range((len(self.snake_segments) - 1), 0, -1):
            new_x = self.snake_segments[seg_index - 1].xcor()
            new_y = self.snake_segments[seg_index - 1].ycor()
            self.snake_segments[seg_index].goto(new_x, new_y)    
        self.head.forward(MOVEMENT)

    def grow_in_size(self)->None:
        """Adds a new segment to a moving snake
        """
        new_segment = Turtle(SNAKE_SHAPE)
        new_segment.color(SNAKE_COLOR)
        new_segment.penup()
        new_segment.goto(self.snake_segments[-1].position())
        self.snake_segments.append(new_segment)
    
    def move_up(self)->None:
        if int(self.head.heading()) != HEAD_DOWN:
            self.head.setheading(HEAD_UP)

    def move_left(self)->None:
        if int(self.head.heading()) != HEAD_RIGHT:
            self.head.setheading(HEAD_LEFT)    

    def move_down(self)->None:
        if int(self.head.heading()) != HEAD_UP:
            self.head.setheading(HEAD_DOWN)

    def move_right(self)->None:
        if int(self.head.heading()) != HEAD_LEFT:
            self.head.setheading(HEAD_RIGHT)

    def reset_position(self)->None:
        """Deletes segments of a snake leaving his initial 3 segments.
        Then sets a snake to it's starting position.
        """
        self.tail_x = 0
        snake_to_hide = self.snake_segments[3:]
        self.snake_segments = self.snake_segments[:3]
        for segment in snake_to_hide:
            segment.hideturtle()
        for segment in self.snake_segments:
            segment.setx(self.tail_x)
            segment.sety(0)
            self.tail_x -= 20
        self.head.setheading(HEAD_RIGHT)
        