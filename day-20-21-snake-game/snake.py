from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_seg = Turtle(shape="square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def eat_food(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.make_snake()
        self.head = self.segments[0]

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

