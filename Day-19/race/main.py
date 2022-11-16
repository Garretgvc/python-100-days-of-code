import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Pick a Turtle", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_index = [-70, -40, -10, 10, 40, 70]
all_turtles = []

for t in range(0, 6):
    new = Turtle(shape="turtle")
    new.color(colors[t])
    new.penup()
    new.speed("fastest")
    new.goto(x=-230, y=y_index[t])
    all_turtles.append(new)

if user_input:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 212:
            winner = turtle.pencolor()
            is_race_on = False
            if winner == user_input:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You lose. The {winner} turtle is the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()