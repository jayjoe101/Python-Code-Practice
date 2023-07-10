import random
rps = ['rock', 'paper', 'scissors']
player = input("Rock, Paper, Scissors: ").lower()
computer = random.choice(rps)

print (f'YOU: {player.upper()} vs COMPUTER: {computer.upper()}')
if player == 'rock' and computer == 'scissors':
    print('You Win')
elif player == 'paper' and computer == 'rock':
    print('You Win')
elif player == 'scissors' and computer == 'paper':
    print('You Win')
else:
    print('You Lose')