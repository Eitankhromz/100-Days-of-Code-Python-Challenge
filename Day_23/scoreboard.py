from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 70, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.right_score = 0
        self.left_score = 0
        self.penup()
        self.ht()

    def show_score(self):
        self.goto(-100, 200)
        self.write(f"{self.left_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.right_score}", align=ALIGNMENT, font=FONT)

    def r_scored(self):
        self.right_score += 1
        self.clear()

    def l_scored(self):
        self.left_score += 1
        self.clear()

