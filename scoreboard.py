from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.goto(0,275)
        self.highscore = 0
        self.score_count = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"S C O R E: {self.score_count} High Score: {self.highscore}", align="center", font=("Verdana", 14, "normal"))

# replacing the game over with reset
    def reset(self):
        if self.score_count>self.highscore:
            self.highscore = self.score_count

        self.score_count=0
        self.update_scoreboard()

    def increase_score(self):
        self.score_count+=1
        self.update_scoreboard()
        # self.clear()
        # self.write(f"S C O R E: {self.score_count} High Score: {self.highscore}", align="center", font=("Verdana", 14, "normal"))



