from turtle import Turtle
ALLIGNMENT = "right"
FONT = ('Arial', 12, "bold")
MOVE = False


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.count = 0
        self.high_score = 0
        self.penup()
        self.goto(250, 260)
        self.ht()
        self.score_board()

    def score_board(self):
        self.clear()
        self.write(f"Score:{self.count} High Score:{self.high_score}", MOVE,
                   ALLIGNMENT, font=FONT)

    def reset_board(self):
        if self.count > self.high_score:
            self.high_score = self.count
        self.count = 0
        self.score_board()

    def add(self):
        self.count += 1
        self.score_board()


