from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

BG_COLOR = "black"
GAME_TITLE = "Pong"
R_STARTING_COORDINATES = (350, 0)
L_STARTING_COORDINATES = (-350, 0)

def screen_setup()->None:
    """Sets up a screen for a pong game
    """
    pong_screen.setup(width = 800, height = 600)
    pong_screen.bgcolor(BG_COLOR)
    pong_screen.title(GAME_TITLE)
    pong_screen.listen()
    pong_screen.onkey(r_paddle.move_up, "Up")
    pong_screen.onkey(r_paddle.move_down, "Down")
    pong_screen.onkey(l_paddle.move_up, "w")
    pong_screen.onkey(l_paddle.move_down, "s")    

pong_screen = Screen()
pong_screen.tracer(0)
r_paddle = Paddle(R_STARTING_COORDINATES)
l_paddle = Paddle(L_STARTING_COORDINATES)
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
screen_setup()

while game_is_on:
    time.sleep(ball.move_speed)
    pong_screen.update()
    ball.move_ball()

    #detect collision with a wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    
    #detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        ball.increase_ball_speed()

    #detect missing the ball
    if(ball.xcor()>380):
        ball.reset_position()
        scoreboard.l_score()
    elif(ball.xcor() < -380):
        ball.reset_position()
        scoreboard.r_score()















pong_screen.exitonclick()