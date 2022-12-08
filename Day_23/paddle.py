from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        if self.ycor() < 240:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if self.ycor() > -240:
            self.goto(self.xcor(), new_y)

