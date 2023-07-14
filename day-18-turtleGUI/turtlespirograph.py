from turtle import Turtle, Screen
import random as r

tuwtle = Turtle()
screen = Screen()
screen.colormode(255)

def rand_color():
    tuwtle.pencolor((r.randint(1,255), r.randint(1,255), r.randint(1,255)))

tuwtle.pensize(2)
tuwtle.speed('fastest')
for n in range(1, 361, 5):
    rand_color()
    tuwtle.circle(100)
    tuwtle.setheading(n)

screen.exitonclick()