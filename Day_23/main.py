import time
import random
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Cross")
screen.tracer(0)
screen.listen()


#Create player
player = Player()

screen.onkeypress(fun=player.move_fd, key="Up")

#Testing out CarManager
carManager = CarManager()
scoreboard = Scoreboard()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    carManager.create_car()

    carManager.move()

    scoreboard.show_score()

    #Check if successfully crossed
    if player.ycor() > 280:
        scoreboard.level_up()
        carManager.increase_speed()
        player.reset_pos()

    #Check if car hit turtle
    for car in carManager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_on = False


screen.exitonclick()

