from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()

    
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.player1_score}", False, align="left", font=("Courier", 24, "normal"))
        self.goto(100, 200)
        self.write(f"{self.player2_score}", False, align="right", font=("Courier", 24, "normal"))
    
    def increase_score(self, player):
        if player == 1:
            self.player1_score += 1
        elif player == 2:
            self.player2_score += 1
        
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over!", False, align="center", font=("Courier", 80, "normal"))