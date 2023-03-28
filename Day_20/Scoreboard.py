from turtle import Turtle
ALLIGNMENT = "right"
FONT = ('Arial', 12, "bold")
MOVE = False

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.goto(250, 260)
        self.count = 0
        self.score_board()

    def score_board(self):
        self.write(f"Score:{self.count}", MOVE, ALLIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", MOVE, "center",
                   font=('Arial', 32, "bold"))

    def add(self):
        self.count += 1
        self.clear()
        self.score_board()


