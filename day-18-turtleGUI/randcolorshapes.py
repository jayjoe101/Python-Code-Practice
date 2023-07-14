from turtle import Turtle, Screen
import random as r

tuwtle = Turtle()
screen = Screen()
screen.colormode(255)
tuwtle.pencolor((r.randint(1,255), r.randint(1,255), r.randint(1,255)))

n = 3
sides = 3
while n < 11:
    tuwtle.forward(100)
    tuwtle.right(360/n)
    sides -= 1
    if sides == 0:
        sides = n + 1
        n += 1
        tuwtle.pencolor((r.randint(1,255), r.randint(1,255), r.randint(1,255)))

screen.exitonclick()