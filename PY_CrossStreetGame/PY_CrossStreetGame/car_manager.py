from turtle import Turtle
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
SHAPE = "square"
X_RANGE = 300
Y_RANGE = list(range(-240,280,20))
HEAD_LEFT = 180

class Car_Manager(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(X_RANGE, choice(Y_RANGE))
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self)->None:
        """Creates a new car and adds it to the list of all cars
        """
        car_color = choice(COLORS)
        x_cor = X_RANGE
        y_cor = choice(Y_RANGE)
        new_car = (Turtle(shape = SHAPE))
        new_car.penup()
        new_car.shapesize(stretch_wid = 1, stretch_len = 2)
        new_car.speed("fastest")
        new_car.setheading(HEAD_LEFT)
        new_car.color(car_color)
        new_car.goto(x_cor, y_cor)
        x_cor -=20
        self.all_cars.append(new_car)
    
    def move_forward(self)->None:
        """Moves all the cars forward
        """
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_speed(self)->None:
        """Increases the speed of a cars
        """
        self.car_speed += MOVE_INCREMENT

    def destroy_car(self)->None:
        """removes first car from the car list
        """
        self.all_cars[0].hideturtle()
        self.all_cars.pop(0)


