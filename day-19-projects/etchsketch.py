from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def foward():
    t.forward(10)

def backward():
    t.backward(10)

def left():
    t.left(10)

def right():
    t.right(10)

def clear():
    screen.clearscreen
    t.reset()

screen.onkeypress(foward, 'w') 
screen.onkeypress(backward, 's')
screen.onkeypress(left, 'a')
screen.onkeypress(right, 'd')
screen.onkey(clear, 'c')
screen.listen()

screen.exitonclick()