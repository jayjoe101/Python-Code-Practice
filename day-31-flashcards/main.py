from tkinter import *
from io import BytesIO
import requests
import pygame
import random as r
import pandas

CARD_COLOR = '#252d45'
CANVAS_COLOR = '#080724'
TEXT_COLOR = '#d5e0ed'


# data

data = pandas.read_csv('words.csv')
data_dict = data.to_dict(orient='records')


# functions
current_card = r.choice(list(data_dict))
clock = None

def next_card():
    global current_card
    current_card = r.choice(list(data_dict))
    flashcard.itemconfig(card_language, text='Polish')
    flashcard.itemconfig(card_word, text=current_card['Polish'])
    timer(5)

def unknown():
    next_card()
    
def known():
    global current_card
    data_dict.remove(current_card)
    next_card()

def pronounciation():
    response = requests.get(current_card['Link'])
    audio_data = BytesIO(response.content)

    pygame.mixer.init()
    pygame.mixer.music.load(audio_data)
    pygame.mixer.music.play()

def timer(count):
    if count > 0:
        global clock
        clock = screen.after(1000, timer, count - 1)
    else:
        global current_card
        flashcard.itemconfig(card_language, text='English')
        flashcard.itemconfig(card_word, text=current_card['English'])


# screen

screen = Tk()
screen.title('5000 Common Polish Words Flashcards')
screen.minsize(width=800, height=526,)
screen.config(padx=50, pady= 50, bg=CANVAS_COLOR)

flashcard = Canvas(width=700, height=426, bg=CARD_COLOR, highlightthickness=0)
card_language = flashcard.create_text(350, 150, text='language', font=('Ariel', 40, 'italic')) # language
card_word = flashcard.create_text(350, 263, text='word', font=('Ariel', 60, 'italic')) # word
flashcard.grid(row=0, column=0, columnspan=5)


# buttons

c = PhotoImage(file='check_image.png')
checkmark = Button(image=c, width= 50, height=50, bg=CANVAS_COLOR, highlightthickness=0, command=known)
checkmark.grid(row=1,column=4)

x = PhotoImage(file='x_image.png')
xmark = Button(image=x, width= 50, height=50, bg=CANVAS_COLOR, highlightthickness=0, command=unknown)
xmark.grid(row=1,column=0)

s = PhotoImage(file='speaker_image.png')
speaker = Button(image=s, width= 50, height=50, bg=CANVAS_COLOR, highlightthickness=0, command=pronounciation)
speaker.grid(row=1,column=2)


# main area

next_card()

screen.mainloop()