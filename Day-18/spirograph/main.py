import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
angle = 0
tim.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for step in range(72):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + 5)

screen = t.Screen()
screen.exitonclick()