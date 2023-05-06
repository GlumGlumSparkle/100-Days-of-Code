from turtle import Turtle
ALLIGNMENT = "center"
FONT_STYLE = ('Courier', 80, 'normal')
MOVE = False


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.goto(50, 180)
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, MOVE, ALLIGNMENT, font=FONT_STYLE)
        self.goto(100, 200)
        self.write(self.r_score, MOVE, ALLIGNMENT, font=FONT_STYLE)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
