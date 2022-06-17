from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.update_score()

    
    def update_score(self):
        self.clear()
        self.goto(-270, 260)
        self.write(f"Level: {self.level}", False, align="left", font=FONT)
        
        
    def increase_score(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over!", False, align="center", font=FONT)