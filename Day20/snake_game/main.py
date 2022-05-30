from turtle import Turtle, Screen
import time
from snake import Snake

from Day20.snake_game.snake import snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()


screen.update()

is_alive = True

while is_alive:
    time.sleep(0.1)
    screen.update()
    snake.move()

screen.exitonclick()