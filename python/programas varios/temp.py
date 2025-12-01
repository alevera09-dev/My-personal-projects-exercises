# -*- coding: utf-8 -*-
"""
Rock Paper Scissors
"""

import random

bot = random.randint(1, 3)
player = input('Rock, Paper or Scissors?(palabra mayuscula, minuscula, o solo letra mayuscula o minuscula) -> ').lower()

def win():
    print('You win')
    print('Bot lose')
    
def draw():
    print('Draw')

def lose():
    print('Bot win')
    print('You lose')
    
def decision(bot):
    if bot == 1:
        print('Bot: Rock')
    elif bot == 2:
        print('Bot: Paper')
    elif bot == 3:
        print('Bot: Scissors')

if player == 'r' or 'rock':
    if bot == 1:
        draw()
    elif bot == 2:
        lose()
    elif bot == 3:
        win()
elif player == 'p' or 'paper':
    if bot == 1:
        win()
    elif bot == 2:
        draw()
    elif bot == 3:
        lose()    
elif player == 's' or 'scissors':
    if bot == 1:
        lose()
    elif bot == 2:
        win()
    elif bot == 3:
        draw()    
    
    
    
    
    
    
    
    
    
    