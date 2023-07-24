from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.set_highscore()
        self.ht()
        self.penup()
        self.color('white')
        self.setpos((0,280))
        self.update()

    def set_highscore(self):
        with open('highscore.txt') as file:
            self.high_score = int(file.read())

    def update(self):
        """will write the score and high score to the screen"""
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=("Arial", 14, "normal"))
    
    def add_score(self):
        """adds 1 point to the score"""
        self.score += 1
        self.update()

    def game_over(self):
        """now will keep highscore"""
        if self.score > self.high_score:
            with open('highscore.txt','w') as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update()