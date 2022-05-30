from turtle import Screen
from snake import Snake
import time


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