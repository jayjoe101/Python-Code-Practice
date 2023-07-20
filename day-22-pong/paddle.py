from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, paddle_side):
        super().__init__()
        self.xcord = 0
        self.ycord = 0
        self.penup()
        self.paddle(paddle_side)
        self.speed('fastest')
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)


    def paddle(self, paddle_side):
        """puts the paddle into position"""
        if paddle_side == 'left':
            self.xcord = -350
            self.goto(self.xcord,0)
        elif paddle_side == 'right':
            self.xcord = 350
            self.goto(self.xcord,0)
        else:
            print('Invalid paddle location')

    def paddle_up(self):
        """moves paddle up"""
        if self.ycord < 240:
            self.ycord += 15
            self.goto(self.xcord,self.ycord)
    
    def paddle_down(self):
        """moves paddle down"""
        if self.ycord > -240:
            self.ycord -= 15
            self.goto(self.xcord,self.ycord)
