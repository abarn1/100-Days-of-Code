from turtle import Turtle


class Scoreboard():
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
    
    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), False, align="left", font=("Arial", 14, "normal"))