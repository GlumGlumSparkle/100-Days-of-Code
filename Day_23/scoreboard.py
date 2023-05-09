from turtle import Turtle
FONT_STYLE = ("Courier", 24, "normal")
TEXT = "GAME OVER"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.ht()
        self.level_value = 1
        self.level()

    def game_over_text(self):
        self.goto(0, 0)
        self.write(TEXT, move=False, align="center", font=FONT_STYLE)

    def game_won(self):
        self.goto(0, 0)
        self.write("YOU WON!", move=False, align="center", font=FONT_STYLE)

    def level(self):
        self.clear()
        self.goto(-270, 250)
        self.write(f"Level:{self.level_value}", move=False, align="left", font=FONT_STYLE)

    def level_update(self):
        self.level_value += 1
        self.level()


