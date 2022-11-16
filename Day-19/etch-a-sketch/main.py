import turtle
from turtle import Turtle, Screen
screen = Screen()
pin = Turtle()


def move_forward():
    pin.forward(10)


def move_backwards():
    pin.backward(10)


def turn_right():
    pin.right(10)


def turn_left():
    pin.left(10)


def clear():
    pin.clear()
    pin.penup()
    pin.home()
    pin.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()

