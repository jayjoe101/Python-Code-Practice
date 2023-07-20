from turtle import Turtle
import random as r

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed('fastest')
        self.respawn()

    def respawn(self):
        """when called will respawn the food to a random location on the map again"""
        self.goto((r.randint(-280,280),r.randint(-280,280)))