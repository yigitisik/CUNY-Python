from turtle import Turtle, Screen
from prettytable import PrettyTable
import random as r

tr = Turtle()
tr.shape("turtle")
directions = [0, 90, 180, 270]
tr.speed(0)

def random_color():
    red = r.random()
    green = r.random()
    blue = r.random()
    return (red, green, blue)


# for side in range(3,6):
#     tr.fillcolor(r.random(), r.random(), r.random())  # for turtle color changes looking funny, Values between 0 and 1
#     tr.pencolor(random_color())
#     angle = 360/side
#     for _ in range(side):
#         tr.fd(40)
#         tr.right(angle)

# for _ in range(20):
#     tr.pensize(5)
#     steps = int(r.random() * 40)
#     tr.color(random_color())
#     tr.fd(steps)
#     tr.setheading(r.choice(directions))

circle_count = int(input("How many circles do you want in the spirograph: "))
for _ in range(circle_count):
    angle = 360/circle_count
    tr.color(random_color())
    tr.circle(40)
    tr.left(angle)

screen = Screen()
screen.exitonclick()


table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Balrok", "Vizigoth"])
table.add_column("Type", ["Fire", "Ice", "Soil"])

print(table)