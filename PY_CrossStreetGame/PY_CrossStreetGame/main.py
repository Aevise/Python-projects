from turtle import Screen
import time
from player import Player
from car_manager import Car_Manager
from scoreboard import Scoreboard


COLOR = "white"
TITLE = "A short tale of Turtle crossing the road"
ITERATIONS_TO_GENERATE_CAR = 6
iteration = 0

def configure_screen()->None:
    screen.setup(width=600, height=600)
    screen.bgcolor(COLOR)
    screen.title(TITLE)
    screen.listen()
    screen.onkey(player.move_forward, "Up")

screen = Screen()
screen.tracer(0)   
player = Player()
scoreboard = Scoreboard()
cars = Car_Manager()
configure_screen()

game_is_on = True
while game_is_on:
    if iteration == ITERATIONS_TO_GENERATE_CAR:
        cars.create_car()
        iteration = 0

    time.sleep(0.1)
    screen.update()
    cars.move_forward()

    #detect collision with a car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.end_screen()
            game_is_on = False
        if car.xcor() < -320:
            cars.destroy_car()

    #detect if player crossed the road
    if player.ycor() > 280:
        player.starting_position()
        scoreboard.next_level()
        cars.increase_speed()

    iteration += 1


screen.exitonclick()