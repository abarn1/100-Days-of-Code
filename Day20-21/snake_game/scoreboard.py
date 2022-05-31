from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 18, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 18, "normal"))