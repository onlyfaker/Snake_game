from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.highscore = 0
        self.score_count = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 275)
        self.color("white")
        self.write(f"Score: {self.score_count} High Score: {self.highscore}", align="center",
                   font=("Verdana", 14, "normal"))

    def reset(self):
        if self.score_count > self.highscore:
            self.highscore = self.score_count
        self.score_count = 0
        self.clear()
        self.update_scoreboard()

    def increase_score(self):
        self.score_count += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write(f"GAME OVER", align="center", font=("Verdana", 24, "normal"))
    #
    # def press_to_reset(self):
    #     self.goto(0, -30)
    #     self.color("white")
    #     self.write(f"PRESS R to RESET", align="center", font=("Verdana", 16, "normal"))