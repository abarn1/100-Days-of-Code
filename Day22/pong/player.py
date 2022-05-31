from turtle import Turtle, position

class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_player(position)
    
    def create_player(self, position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)
        self.setheading(90)
    
    def move_up(self):
        self.forward(20)
    
    def move_down(self):
        self.backward(20)