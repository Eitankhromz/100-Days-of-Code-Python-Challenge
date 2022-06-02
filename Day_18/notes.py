# [keyword] [module] [keyword] [Class]
from turtle import Turtle, Screen
import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")

# Draw a square
# for _ in range(4):
#     tim.fd(100)
#     tim.right(90)
#     tim.penup()

# Draw a dashed line
# for num in range(101):
#     if num % 2 == 0:
#         tim.penup()
#     else:
#         tim.pendown()
#     tim.fd(5)

# for num in range(15):
#     tim.fd(10)
#     tim.penup()
#     tim.fd(10)
#     tim.pendown()

# Draw Triangle, Square, Pentagon ....
import random
colors = ["red", "green", "blue", "orange", "black", "purple", "teal", "magenta", "salmon", "pink"]
# degree = 0
# for shape in range(3, 11):
#     degree = 360/shape
#     random_color = random.choice(colors)
#     tim.color(random_color)
#     for _ in range(shape):
#         tim.fd(100)
#         tim.right(degree)


# def create_shapes(num_sides):
#     degree = 360 / num_sides
#     for _ in range(num_sides):
#         tim.fd(100)
#         tim.right(degree)
#
#
# for shape in range(3, 11):
#     tim.color(random.choice(colors))
#     create_shapes(shape)

t.colormode(255)


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tuple = (r, g, b)
    return tuple


# def random_walk(walk):
#     directions = [0, 90, 180, 270]
#     degree = random.choice(directions)
#     tim.pensize(10)
#     tim.speed("fastest")
#
#     for steps in range(walk):
#         my_tuple = random_color()
#         tim.pencolor(my_tuple)
#         tim.fd(30)
#         tim.setheading(random.choice(directions))
#
#
# random_walk(500)


def create_circle(rotations):
    tim.speed("fastest")
    for circle in range(rotations):
        tim.pencolor(random_color())
        degree = 360/rotations
        tim.circle(100)
        tim.right(degree)


create_circle(1000)

screen = Screen()
screen.exitonclick()
