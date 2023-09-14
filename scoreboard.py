from turtle import *

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-100, 250)
        self.write(arg=f"Score : {self.score}", align="right", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER!!!!!!!:(", align="center", font=FONT, move=False)

    def nxt_lvl(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score : {self.score}", align="right", font=FONT)
