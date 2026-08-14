from turtle import Turtle
PLACEMENT_X, PLACEMENT_Y = -250, 270
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(PLACEMENT_X, PLACEMENT_Y)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def scoreboard_increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER, SCORE: {self.level}", align="center", font=FONT)

