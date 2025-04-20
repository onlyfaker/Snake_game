from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.goto(0,275)
        self.score_count = 0
        self.write(f"S C O R E: {self.score_count}", align="center", font=("Verdana", 14, "normal"))

    def increase_score(self):
        self.clear()
        self.write(f"S C O R E: {self.score_count}", align="center", font=("Verdana", 14, "normal"))


