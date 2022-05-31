from turtle import Turtle

class Player():

    def __init__(self, player_number):
        super().__init__()
        self.player_number = player_number
        self.segments = []
    
    def create_player():
        for i in range(4):
            self.segments.append(Turtle("square"))
            self.segments[i].color("white")
            self.segments[i].penup()
            self.segments[i].speed("fastest")
            self.segments[i].goto(self.xcor(), self.ycor() + 20 * i)
