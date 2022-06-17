from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")

screen.update()

is_alive = True

while is_alive:
    time.sleep(0.05)
    screen.update()
    snake.move()

    # Detect collision with food
    if snake.head.distance(food.pos()) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    
    # Detect collision with border
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.game_over()

    # Detect collision with itself
    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10:
            scoreboard.reset()    
screen.exitonclick()