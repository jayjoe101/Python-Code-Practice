from turtle import Turtle, Screen
import pandas as p

screen = Screen()
screen.setup(width=725, height=491)
screen.bgpic('blank_states_img.gif')

states_data = p.read_csv('50_states.csv')

states = []
for state in states_data.state.values:
    states.append(state.lower())

lives = 10
correct_guesses = 0

game_is_on = True
while game_is_on:

    t = Turtle(visible=False)
    t.penup()

    player_guess = screen.textinput('Player_Guess', f'Lives = {lives}\nEnter a State Name:')
    if str(player_guess).lower() in states:
        guessed_state = str(player_guess).lower()
        guessed_state = guessed_state[0].upper() + guessed_state[1:]
        
        xcord = states_data[states_data.state == guessed_state].x.values[0]
        ycord = states_data[states_data.state == guessed_state].y.values[0]
        
        t.goto(xcord,ycord)
        t.write(guessed_state)
        
        correct_guesses += 1
    else:
        lives -= 1

    if lives == 0:
        t.goto(0,0)
        t.color('red')
        t.write("YOU SUCK AND LOST HAHA", font=('comicsans',20,'normal'), align='center')
        game_is_on = False
    if correct_guesses == 50:
        t.goto(0,0)
        t.color('green')
        t.write("Chad winner, you won!", font=('comicsans',20,'normal'), align='center')
        game_is_on = False


screen.exitonclick()