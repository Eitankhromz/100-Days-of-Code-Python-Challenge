#Extracting colors from image:
# import colorgram as c
#
# colors = c.colorgram
# list_colors = colors.extract('image.jpg', 30)
#
# list_rgb = []
# for index in range(len(list_colors)):
#     rgb = list_colors[index].rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     tupil = (r, g, b)
#     list_rgb.append(tupil)
#
# print(list_rgb)


import turtle as t
from turtle import Screen
import random

t.colormode(255)
color_list = [(243, 232, 66), (251, 230, 236), (216, 237, 244), (196, 76, 32), (218, 67, 107), (195, 175, 18), (18, 125, 173), (13, 143, 89), (108, 182, 209), (13, 167, 214), (206, 153, 93), (239, 232, 3), (24, 39, 74), (183, 43, 63), (36, 44, 110), (77, 174, 96), (214, 68, 49), (217, 130, 153), (124, 185, 120), (237, 162, 181), (6, 60, 38), (148, 209, 220), (7, 92, 52), (5, 86, 110), (162, 28, 26), (235, 170, 163), (155, 215, 187)]
tim =t.Turtle()

screen = Screen()

tim.penup()
tim.setposition(-370, -300)
tim.speed("fastest")

def straight():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.fd(50)

for _ in range(10):
    straight()
    tim.setheading(90)
    tim.fd(50)
    tim.setheading(180)
    tim.fd(500)
    tim.setheading(0)


screen.exitonclick()
