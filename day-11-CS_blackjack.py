import random
import os
import time

deck = {
    'Spades': ['A','2','3','4','5','6','7','8','9','10','J','Q','K'],
    'Clubs': ['A','2','3','4','5','6','7','8','9','10','J','Q','K'],
    'Diamonds': ['A','2','3','4','5','6','7','8','9','10','J','Q','K'],
    'Hearts': ['A','2','3','4','5','6','7','8','9','10','J','Q','K'],
}

def shuffle():
    """resets the deck"""
    for cards in deck:
        deck[cards] = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

def get_card():
    """returns a card"""
    random_suit = random.choice(list(deck.keys()))
    card = random.choice(deck[random_suit])
    deck[random_suit].remove(card)
    return card

def add_card(lst, n):
    """adds specified amount of cards to a deck"""
    for i in range(n):
        lst.append(get_card())
    return lst

def card_value(d):
    """calculates the total value of a deck"""
    value = 0
    for c in d:
        if c == 'K' or c == 'Q' or c == 'J':
            value += 10
        elif c == 'A':
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
        else:
            value += int(c)
    return value

def print_screen(pd,cd,p,c):
    """prints the 'ui' to the screen"""
    os.system('cls')
    
    print(f'Your cards: {pd}')
 
    print(f'Your cards Value: {p}')    
    
    print(f'Dealer cards: {cd}')
    print(f'Dealer cards value: {c}')
 

def blackjack():
    
    player_deck = []
    computer_deck = []

    add_card(player_deck, 2)  
    add_card(computer_deck, 1)
    
    player = card_value(player_deck)
    computer = card_value(computer_deck)
    
    while True:
        
        print_screen(player_deck,computer_deck,player,computer)
        
        
        if player < 21 and input('"h" to hit "s" to stand: ') == 'h':
            add_card(player_deck, 1)
            player = card_value(player_deck)
        else:
            while computer < 17:
                time.sleep(1)
                add_card(computer_deck, 1)
                computer = card_value(computer_deck)
                print_screen(player_deck,computer_deck,player,computer)
            if player > 21 and computer > 21:
                print('Both busted')
            if player > 21:
                print('Busted, You lose')
            elif computer > 21:
                print('Dealer busts, your win')
            elif computer > player:
                print('Dealer wins')
            else:
                print('Player wins')
            break
    
    if input('Want to keep playing? ("y" or "n"): ') == 'y':
        shuffle()
        blackjack()

blackjack()