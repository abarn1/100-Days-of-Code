from turtle import Turtle

class Ball:
    def __init__(self):
        super.__init__()
        self.shape("square")
        self.color("white")
    
    def move(self):
        self.fd(10)
    
    def bounce(self):
        self.rt(180)

    