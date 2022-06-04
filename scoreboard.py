from turtle import Turtle

ALIGNMENT = "center"
FONT_NAME = "Courier"
FONT_SIZE = 20
FONT_WEIGHT = "bold"
NORMAL = (FONT_NAME, FONT_SIZE, FONT_WEIGHT)
LARGE = (FONT_NAME, FONT_SIZE * 2, FONT_WEIGHT)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.x = 0
        self.y = 260
        self.pu()
        self.goto(self.x, self.y)
        self.hideturtle()
        self.update()

    def update(self):
        text = f"LEVEL: {self.level}"
        self.write(arg=text, align=ALIGNMENT, font=NORMAL)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        text = "GAME OVER"
        self.write(arg=text, align=ALIGNMENT, font=LARGE)
