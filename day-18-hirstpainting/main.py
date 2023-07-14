import colorgram
import random as r
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.colormode(255)
screen.setup (width=500, height=500, startx=0, starty=0)

colors = colorgram.extract('canal_image.jpg', 10)

t.penup()
t.ht()
row_pos = 25
t.speed('fastest')
for _ in range(10):
    for _ in range(10):
        t.dot(15, r.choice(colors).rgb)
        t.forward(25)
    t.setposition((0, row_pos))
    row_pos += 25

screen.exitonclick()