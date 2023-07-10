import game_data
import art # you should import like from art import logo, vs
import random
import os

def get_influencer():
    return random.choice(game_data.data)

def print_screen(inf_1, inf_2, score):
    os.system('cls')
    print(art.logo)
    if score:
        print("You're right!", end = ' ')
    print(f'Current score: {score}')
    print(f"Compare A: {inf_1['name']}, a {inf_1['description']}, from {inf_1['country']} ")
    print(art.vs)
    print(f"Against B: {inf_2['name']}, a {inf_2['description']}, from {inf_2['country']} ")

def higher_lower():
    score = 0

    while True:

        influencer_1 = get_influencer()
        influencer_2 = get_influencer()

        followers_1 = influencer_1['follower_count']
        followers_2 = influencer_2['follower_count']

        print_screen(influencer_1, influencer_2, score)
        choice = input('Who has more followers "A" or "B": ')
        if choice == 'A' and followers_1 > followers_2:
            score += 1
        elif choice == 'B' and followers_1 < followers_2:
            score += 1
        else:
            print(f'Incorrect, You lose. Final Score: {score}')
            break
    
    if input('Want to play again "y" or "n": ') == 'y':
        higher_lower()

higher_lower()