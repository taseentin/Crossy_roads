from turtle import *

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.go_to_start()
        self.shape("turtle")
        self.left(90)

    def dodge(self):
        self.forward(MOVE_DISTANCE)
        """if self.ycor()==FINISH_LINE_Y:
            self.goto(STARTING_POSITION)"""

    def finished(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    pass
