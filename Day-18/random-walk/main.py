import turtle as t
import random

tim = t.Turtle()
tim.speed(0)
tim.pensize(15)
directions = [0, 90, 180, 270]
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_walk():
    tim.pencolor(random_color())
    tim.setheading(random.choice(directions))
    tim.forward(50)


for turns in range(200):
    random_walk()