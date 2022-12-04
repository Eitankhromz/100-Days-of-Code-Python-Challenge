from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_fd():
    t.fd(10)


screen.listen()
screen.onkey(key="space", fun=move_fd)
#when passing a function as an imput, do not include parentheses
#make sure to use positional arguments


screen.exitonclick()
