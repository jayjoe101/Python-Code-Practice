from turtle import Turtle
import random as r

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.serve_ball()

    def serve_ball(self):
        """moves the ball to a random side once the game starts"""
        self.goto(0,0)
        if r.randint(1,2) == 1:
            if r.randint(1,2) == 1:
                self.setheading(35)
            else:
                self.setheading(-35)
        else:
            if r.randint(1,2) == 1:
                self.setheading(215)
            else:
                self.setheading(-215)

    def paddle_bounce(self):
        """the logic of where the ball will go after a collision"""
        self.setheading((self.heading() * -1) + 180)

    def wall_bounce(self):
        """bounce logic on wall"""
        self.setheading(self.heading() * -1)
