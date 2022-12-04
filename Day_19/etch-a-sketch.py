from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.fd(10)


def move_backwards():
    tim.back(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
 
#OR

def reset():
    t.reset()



screen.listen()
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
