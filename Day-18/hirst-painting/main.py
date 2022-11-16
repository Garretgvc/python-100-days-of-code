# import colorgram
#
# colors = colorgram.extract('sample-image.jpg', 20)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     true_color = (r, g, b)
#     rgb_colors.append(true_color)
#
# print(rgb_colors)
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed(0)
tim.hideturtle()
color_list = [(244, 237, 222), (243, 234, 240), (232, 242, 237), (192, 165, 115), (138, 166, 190), (56, 102, 140),
              (141, 91, 50), (12, 23, 55), (222, 207, 123), (182, 154, 42), (61, 22, 11), (182, 146, 165),
              (142, 177, 151), (72, 117, 81), (58, 15, 26), (126, 79, 102), (130, 30, 16), (15, 39, 23), (24, 53, 127)]
tim.penup()
tim.setheading(225)
tim.forward(380)
tim.setheading(0)
dot_count = 101

for step in range(1, dot_count):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if step % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
