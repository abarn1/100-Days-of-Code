from player import Player
from ball import Ball
from scoreboard import Scoreboard
from turtle import Screen
from time import sleep

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()


player1 = Player((-350, 0))
player2 = Player((350, 0))
ball = Ball()
score = Scoreboard()


screen.onkeypress(player1.move_up, "w")
screen.onkeypress(player1.move_down, "s")

screen.onkeypress(player2.move_up, "Up")
screen.onkeypress(player2.move_down, "Down")


game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    # Detect collision with border
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    # Detect collision with players
    if (ball.xcor() < -330 and ball.distance(player1) < 50) or (ball.xcor() > 330 and ball.xcor() < 360 and ball.distance(player2) < 50):
        ball.player_bounce()
    # Detect when player 1 scores
    if ball.xcor() > 370:
        score.increase_score(1)
        ball.reset_ball()
        ball.player_bounce()
    # Detect when player 2 scores
    if ball.xcor() < -370:
        score.increase_score(2)
        ball.reset_ball()
        ball.player_bounce()

    if score.player1_score == 5 or score.player2_score == 5:
        game_is_on = False
        score.game_over()

    
    sleep(ball.move_speed)

    












screen.exitonclick()