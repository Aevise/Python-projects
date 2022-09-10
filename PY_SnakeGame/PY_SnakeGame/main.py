from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

BG_COLOR = "black"
GAME_TITLE = "Snake Game"


def screen_setup():
    """Sets up a screen for a snake game
    """
    snake_screen.setup(width=600, height=600)
    snake_screen.bgcolor(BG_COLOR)
    snake_screen.title(GAME_TITLE)
    snake_screen.listen()
    snake_screen.onkey(snake.move_up, "Up")
    snake_screen.onkey(snake.move_down, "Down")
    snake_screen.onkey(snake.move_left, "Left")
    snake_screen.onkey(snake.move_right, "Right")
    
snake_screen = Screen()
snake_screen.tracer(0)
game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen_setup()

while game_is_on:
    snake_screen.update()
    time.sleep(0.1)
    snake.move_snake()

    #collision with food
    if snake.head.distance(food) < 15:
        snake.grow_in_size()
        food.place_new_food()
        scoreboard.add_score()

    #collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.hit_wall()
        snake.reset_position()
        scoreboard.highest_score()
        time.sleep(5)
        scoreboard.refresh()

    #collision with tail
    for segment in snake.snake_segments[1:]:
        if(snake.head.distance(segment) < 10):
            scoreboard.hit_tail()
            snake.reset_position()
            scoreboard.highest_score()
            time.sleep(5)
            scoreboard.refresh()
    
snake_screen.exitonclick()
