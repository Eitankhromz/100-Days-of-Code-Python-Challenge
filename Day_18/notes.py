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


#OR

#from module import class
#OR
#from turtle import * // imports everything
#from turtle import Turtle #this is recommended tho

from turtle import Screen
import turtle as t
import random

#object = Class()
tim = t.Turtle()
tim.shape("turtle")
tim.color("green")
# timmy_the_turtle.fd(100)
# timmy_the_turtle.right(90)

#DRAW A SQUARE
# for _ in range(4):
#     tim.fd(100)
#     tim.right(90)

# import heroes
# print(heroes.gen())


#DRAW A DOTTED LINE
# for num in range(50):
#     if num % 2 == 0:
#         tim.pd()
#     else:
#         tim.up()
#     tim.fd(5)


#DRAW SHAPES
# sides = 4
#
# while sides < 11:
#     for _ in range(sides):
#         angle = 360/sides
#         tim.fd(100)
#         tim.right(angle)
#     sides += 1
#     tim.color(random.choice(["red", "yellow", "blue", "pink"]))
#OR
# colors = ["red", "blue", "yellow", "brown", "black", "purple"]
#
#
# def draw_shape(num):
#     for _ in range(num):
#         angle = 360 / num
#         tim.fd(100)
#         tim.right(angle)
#
#
# for sides in range(3, 11):
#     draw_shape(sides)
#     tim.color(random.choice(colors))


#Have to tap into module to change tuple range to 255
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple = (r, g, b)
    return tuple


#RANDOM WALK
# tim.pensize(15)
# tim.speed('fastest')
#
# direction = [0, 90, 180, 270]
#
# for _ in range(100):
#     tim.color(random_color())
#     tim.fd(30)
#     tim.setheading(random.choice(direction))

#TUPLES
# my_tuple = (1, 8, 52)
# print(my_tuple[2]) # will print 52
# #change tuple into list:
# list(my_tuple)

#DRAW SPIROGRAPH
# tim.speed('fastest')
#
#
# def draw_spirograph(tilt):
#     for _ in range(int(360/tilt)):
#         tim.circle(100)
#         tim.color(random_color())
#         tim.setheading(tim.heading() + tilt)
#
#
# draw_spirograph(50)



screen = Screen()
screen.exitonclick()

