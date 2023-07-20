from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.middle()
        self.lscore = 0
        self.rscore = 0
        self.left_score()
        self.right_score()

    def middle(self):
        """initializes the middle line on the screen"""
        self.goto(0,-600)
        self.color('white')
        self.shapesize(stretch_len=.25, stretch_wid=.5)
        for n in range(-320,320,20):
            self.goto(0,n)
            self.stamp()
        self.ht()

    def left_score(self):
        """controls the left player score"""
        self.goto(-50,220)
        self.color('blue')
        self.write(f'{self.lscore}', align='center', font=("Arial", 60, "normal"))

    def right_score(self):
        """controls the right player score"""
        self.goto(50,220)
        self.color('red')
        self.write(f'{self.rscore}', align='center', font=("Arial", 60, "normal"))

    def add_rscore(self):
        """adds a point to the right player"""
        self.clear()
        self.middle()
        self.rscore += 1
        self.left_score()
        self.right_score()

    def add_lscore(self):
        """adds a point to the left player"""
        self.clear()
        self.middle()
        self.lscore += 1
        self.left_score()
        self.right_score()

    def game_over(self):
        self.setpos((0,0))
        if self.lscore > self.rscore:
            self.color('blue')
            self.write(f'LEFT PLAYER WINS', align='center', font=("Arial", 40, "normal"))
        else:
            self.color('red')
            self.write(f'RIGHT PLAYER WINS', align='center', font=("Arial", 40, "normal"))