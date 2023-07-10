import random

def get_random_num():
    """generates random num from 1 to 100"""
    return random.choice(range(1, 101))

def guessing_game():
    difficulty = input('Choose a difficulty, "easy" or "hard": ')
    lives = 5
    if difficulty == 'easy':
        lives = 10
    secret_number = get_random_num()    
    
    while lives > 0:
        print(f'Your have {lives} attempts to guess the number')
        player_guess = int(input('Make a guess: '))

        if player_guess == secret_number:
            print('YOU WIN')
            break
        elif player_guess < secret_number:
            print('Too low')
            lives -= 1
        else:
            print('Too high')
            lives -= 1
    
    if input('Want to play again? "y" or "n": ') == 'y':
        guessing_game()

guessing_game()