import time
from turtle import Screen
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player_turtle = Player()
car_manager = CarManager()
score = Scoreboard()

screen.onkeypress(player_turtle.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if player_turtle.ycor() >= 280:
        player_turtle.level_up()
        score.increase_score()
        car_manager.increase_speed()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player_turtle) <20:
            game_is_on = False
            score.game_over()
    screen.update()


screen.exitonclick()