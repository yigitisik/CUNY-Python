from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        # '/Users/mustafayigitisik/high_score_data copy.txt'
        # '/Users/mustafayigitisik/PythonProjects/day20-21 snake game/main.py'
        with open("../../high_score_data copy.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color("Yellow")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, highest score: {self.high_score}", align = "center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../../high_score_data copy.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
