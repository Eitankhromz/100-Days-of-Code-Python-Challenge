from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.setpos(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.speed
            car.goto(new_x, car.ycor())

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    # def check_pos(self):
    #     index = 1
    #     for car in self.all_cars:
    #         if self.all_cars[index-1].xcor() == self.all_cars[index].xcor():
    #             self.all_cars[index].setx(self.all_cars[index].xcor() + 5)




