import colorgram
import turtle as tur
import random as rand


# rgb_colors = []
# colors = colorgram.extract('spot_paint.jpg', 9)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
#above extraction gives below list, excluding 3 of which due to sheer color pick
color_list = [(237, 247, 252), (226, 147, 98), (28, 102, 177), (161, 56, 90), (148, 79, 51), (225, 61, 96)]

tur.colormode(255)  # Enable RGB mode
tr = tur.Turtle()
tr.hideturtle()
tr.speed(0)  # Fastest drawing speed
tr.penup()
sc = tur.Screen() # Set up screen


def spot_paint(horizontal, vertical, radius, distance_between_spot):
    start_x = - (horizontal * distance_between_spot) // 2
    start_y = - (vertical * distance_between_spot) // 2

    for y in range(vertical):
        for x in range(horizontal):
            tr.goto(start_x + x * distance_between_spot, start_y + y * distance_between_spot)
            tr.dot(radius,rand.choice(color_list))


def user_interface():
    horizontal = int(input("How many dots you'd like horizontally: "))
    vertical = int(input("How many dots you'd like vertically: "))
    radius = int(input("Radius of the dots: "))
    distance_between_spot = int(input("Distance between spots: "))

    spot_paint(horizontal, vertical, radius, distance_between_spot)
    sc.exitonclick()

user_interface()