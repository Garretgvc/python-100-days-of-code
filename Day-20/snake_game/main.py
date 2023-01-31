from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

game_speed = 0.1


def speed_up():
    global game_speed
    game_speed += 0.01


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(speed_up(), "Z")

game_on = True
while game_on:
    screen.update()
    time.sleep(game_speed)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    # Detect collision with tale
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
