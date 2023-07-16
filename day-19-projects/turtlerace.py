from turtle import Turtle, Screen
import random as r

screen = Screen()
screen.title("Turtle Race")
screen.setup(width=500, height=515)
screen.colormode(255)

def rand_color(turtle):
    turtle.fillcolor((r.randint(1,255), r.randint(1,255), r.randint(1,255)))

def gen_turtles(turtles):
    turtle_list = []
    for _ in range(int(turtles)):
        turtle_list.append(Turtle(shape="turtle"))
    return turtle_list

def set_positions(turtle_list):
    position = -235
    for turtle in turtle_list:
        rand_color(turtle)
        turtle.penup()
        turtle.setposition(-240, position)
        position += 20

def random_move(turtle_list):
    for turtle in turtle_list:
        turtle.forward(r.randint(5,25))

def race(turtles, bet):
    race = True
    while race:
        random_move(turtles)
        for n in range(len(turtles)):
            if turtles[n].xcor() > 215:
                print(f'Turtle number {n+1} WON!')
                if n+1 == bet:
                    print('YOU WON THE BET')
                else:
                    print('You lost the bet')
                race = False


num = screen.numinput('Number of Turtles', 'How many turtles do you want to race? (max 25)', minval=2, maxval = 25)
bet = screen.numinput('Set the Bet', f'What turtle (1-{str(num).split(".")[0]}) do you think will win?', maxval = num)
turtles = gen_turtles(num)
set_positions(turtles)
race(turtles, bet)

screen.exitonclick()