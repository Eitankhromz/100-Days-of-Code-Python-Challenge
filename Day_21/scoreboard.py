from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.ht()
        self.update_score()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GET FUCKED", True, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.update_scoreboard()
        self.score += 1





