from turtle import Turtle
import random as r

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.car_position()
        self.car_color()
        self.car_speed = 1
        self.shape('square')
        self.shapesize(stretch_len=2)

    def car_color(self):
        self.fillcolor((r.randint(1,255), r.randint(1,255), r.randint(1,255)))

    def car_position(self):
        self.setheading(180)
        self.goto(r.randint(320,920),r.randint(-275,275))
    
    def move(self):
        self.forward(self.car_speed)

    def increase_speed(self, n):
        self.car_speed = n
