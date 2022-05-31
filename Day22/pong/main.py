from player import Player
from ball import Ball
from scoreboard import Scoreboard
from turtle import Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

player1 = Player(1)

screen.exitonclick()