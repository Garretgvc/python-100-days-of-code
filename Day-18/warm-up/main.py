from turtle import Turtle, Screen

tim = Turtle()
tim.shape("classic")
tim.color("green")

# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# tim.pencolor("red")
# for _ in range(3):
#     tim.forward(100)
#     tim.right(120)
#
# tim.pencolor("blue")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# tim.pencolor("green")
# for _ in range(5):
#     tim.forward(100)
#     tim.right(72)
#
# tim.pencolor("yellow")
# for _ in range(6):
#     tim.forward(100)
#     tim.right(60)
#
# angle = 360 / 7
#
# tim.pencolor("orange")
# for _ in range(7):
#     tim.forward(100)
#     tim.right(angle)
#
# tim.pencolor("purple")
# for _ in range(8):
#     tim.forward(100)
#     tim.right(45)

import random

shape_color = ["pink", "red", "orange", "yellow", "green", "blue", "violet", "black"]


def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for sides in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)


for shape in range(3, 11):
    tim.pencolor(random.choice(shape_color))
    draw_shape(shape)

screen = Screen()
screen.exitonclick()
