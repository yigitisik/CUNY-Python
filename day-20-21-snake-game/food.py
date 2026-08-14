from turtle import Turtle
import random as rn


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(rn.randrange(-280, 280), rn.randrange(-280, 280))

