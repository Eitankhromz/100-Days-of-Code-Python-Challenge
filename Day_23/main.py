from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

RIGHT = (350, 0)
LEFT = (-350, 0)

#1. Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

#2. Create and move a paddle
screen.listen()
r_paddle = Paddle(RIGHT)
l_paddle = Paddle(LEFT)

#Move right paddle
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")

#Move left paddle
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")

#Create Ball
ball = Ball()

# Create Scoreboard
score = Score()

game_on = True

while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    score.show_score()

    #Detect Collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect Collision with paddles
    if ball.distance(r_paddle) < 55 and ball.xcor() > 320 or ball.distance(l_paddle) < 55 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect if right player misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_scored()


    #Detect if left player misses ball
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_scored()


screen.exitonclick()

