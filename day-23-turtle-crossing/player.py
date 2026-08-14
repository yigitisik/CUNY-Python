from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.set_player_to_orig_pos()

    def move(self):
        if self.ycor()<280:
            self.fd(MOVE_DISTANCE)

    def move_left(self):
        if self.xcor() >= -360:
            self.left(MOVE_DISTANCE)

    def move_right(self):
        if self.xcor() <= 360:
            self.right(MOVE_DISTANCE)

    def is_player_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def set_player_to_orig_pos(self):
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()