from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.xdir = 10
        self.ydir = 10
        self.move_speed = 0.1
    
    def create_ball(self):
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, 0)
        self.setheading(45)
        
    def reset_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.1
    
    def move(self):
        self.goto(self.xcor() + self.xdir, self.ycor() + self.ydir)
    
    def wall_bounce(self):
        self.ydir *= -1
    
    def player_bounce(self):
        self.xdir *= -1
        self.move_speed *= 0.9
        

    