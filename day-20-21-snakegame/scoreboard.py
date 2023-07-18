from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.color('white')
        self.setpos((0,280))
        self.write_score()

    def write_score(self):
        self.write(f'Score: {self.score}', align='center', font=("Arial", 14, "normal"))
    
    def add_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def game_over(self):
        self.clear()
        self.setpos((0,0))
        self.write(f'YOU LOST!\nFinal Score: {self.score}', align='center', font=("Arial", 14, "normal"))