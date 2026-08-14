from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

sc = Screen()
sc.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
sc.bgcolor("black")
sc.title("Pong")
sc.tracer(0)

right_paddle = Paddle((SCREEN_WIDTH/2 - 50, 0))
left_paddle = Paddle((-SCREEN_WIDTH/2 + 50, 0))
ball = Ball((0,0))
scoreboard = Scoreboard()

sc.listen()
sc.onkeypress(right_paddle.go_up, "Up")
sc.onkeypress(right_paddle.go_down, "Down")
sc.onkeypress(left_paddle.go_up, "w" or "W")
sc.onkeypress(left_paddle.go_down, "s" or "S")

is_game_on = True
while is_game_on:
    time.sleep(ball.moving_speed)
    sc.update()
    ball.move()
    
    #detect collision with up/down wall
    if ball.ycor() > (SCREEN_HEIGHT/2) - 20 or ball.ycor() < -(SCREEN_HEIGHT/2) + 20:
        ball.bounce_y()

    #detect collision with paddle
    if ((ball.distance(right_paddle) < 55 and ball.xcor() > (SCREEN_HEIGHT/2) + 20) or
            (ball.distance(left_paddle) < 55 and ball.xcor() < -(SCREEN_HEIGHT/2) - 20)):
            ball.bounce_x()


    #detect when paddle misses ball
    if ball.xcor() > (SCREEN_WIDTH/2) - 20:
        ball.reset_position()
        scoreboard.left_win_point()
    elif ball.xcor() < -(SCREEN_WIDTH/2) + 20:
        ball.reset_position()
        scoreboard.right_win_point()


sc.exitonclick()