import math
def paint_calc(height, width, cover):
    cans = math.ceil(width * height / cover)
    print(f"You'll need {cans} cans of paint.")
#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)  