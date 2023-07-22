from turtle import Turtle
import random as r

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('White')
        self.start_position_y = -260
        self.start_position_x = 0

    def set_position(self):
        self.start_position_x = r.randint(-300,300)
        self.goto(self.start_position_x,self.start_position_y)

    def move_up(self):
        if self.ycor() < 275:
            self.setheading(90)
            self.forward(5)

    def move_down(self):
        if self.ycor() > -275:
            self.setheading(270)
            self.forward(5)

    def move_left(self):
        if self.xcor() > -275:
            self.setheading(180)
            self.forward(5)

    def move_right(self):
        if self.xcor() < 275:
            self.setheading(0)
            self.forward(5)