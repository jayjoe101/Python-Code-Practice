from turtle import Turtle, Screen
import random as r

tuwtle = Turtle()
screen = Screen()
screen.colormode(255)

def rand_color():
    tuwtle.pencolor((r.randint(1,255), r.randint(1,255), r.randint(1,255)))

tuwtle.speed('fastest')
tuwtle.pensize(5)
for _ in range(100):
    rand_color()
    tuwtle.setheading(r.choice([0, 90, 180, 270]))
    tuwtle.forward(25)

screen.exitonclick()