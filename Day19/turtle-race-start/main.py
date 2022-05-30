from socketserver import StreamRequestHandler
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=800, height=600)
user_bet = screen.textinput(title="Bet input", prompt="Which color would you like to bet on?")
is_race_on = False
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black"]
list_of_turtles = []
num_of_turtles = 6


for count in range(num_of_turtles):
    turtle = Turtle()
    turtle.color(colors[count])
    turtle.penup()
    turtle.goto(-380, (count - num_of_turtles/2) * 50)
    turtle.shape("turtle")
    turtle.pendown()
    count += 1
    list_of_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for tut in list_of_turtles:
        distance_to_move = random.randint(0,20)
        tut.forward(distance_to_move)
        if tut.xcor() > 380:
            is_race_on = False
            if tut.pencolor() == user_bet:
                print("You chose the correct turtle!!")
                break
            else:
                print(f"You chose the wrong turtle. The correct turtle was {tut.pencolor()}")
                break

screen.exitonclick()