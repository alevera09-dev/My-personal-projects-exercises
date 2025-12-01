# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 17:55:19 2025

@author: alesa
"""

# -*- coding: utf-8 -*-
"""
Rock Paper Scissors
"""

import random as ran

# Definir opciones para el bot y opcion de salida
options = {'rock':'🪨', 'paper':'📄', 'scissors':'✂️'}
options_keys = list(options.keys()) 
exit_game = False

# bucle para seguir jugando hasta que el jugador decida
while exit_game != True:
    # hacer que el bot eliga aleatoriamente
    bot_choice = ran.choice(options_keys)
    bot_choice_two = options.get(bot_choice)
    
    #Dar instrucciones
    print('\n|Rock = R/r, ROCK/Rock/rock.| \n|Paper= P/p, PAPER/Paper/paper.|'
          '\n|Scissors = S/s, SCISSORS/Scissors/scissors.| \n|Exit = X/x, EXIT/Exit/exit.|')
    
    # Pedir la opcion al jugador, volverlo a minusculas para que sea mas sencillo compararlos
    player_input = input('\n\t.:Que Eliges:. -> ').lower() 
    
    # comparar la entrada del usuario
    if player_input in ['r', 'rock']:
        player_choice = 'rock'
        player_output = '🪨'
    elif player_input in ['p', 'paper']:
        player_choice = 'paper'
        player_output = '📄'
    elif player_input in ['s', 'scissors']:
        player_choice = 'scissors'
        player_output = '✂️'
    elif player_input in ['x', 'exit']:
        player_choice = 'exit'
    else:
        print("\n.:Entrada no válida. Por favor, elige de nuevo:.")
        player_choice = None
    
    # logica del juego
    if player_choice:
        print(f"\n.:Elegiste: {player_output}:.")
        print(f".:El bot eligió: {bot_choice_two}:.")
        
        if player_choice == bot_choice:
            print("\n|DRAW =/|")
        elif (player_choice == 'rock' and bot_choice == 'scissors') or \
            (player_choice == 'paper' and bot_choice == 'rock') or \
            (player_choice == 'scissors' and bot_choice == 'paper'):
                print("\n|YOU WIN =) |")
        elif player_choice == 'exit':
            exit_game = True
        else:
            print("\n|YOU LOSE =(|")


print('\n\t\t| Gracias jugar!!! |')





"""
#Prueba de aleatoridad del bot
options = ['rock', 'paper', 'scissors']
rock_choice = 0
paper_choice = 0
scissors_choice = 0
intentos = 0

while intentos < 10:
    bot_choice = ran.choice(options)
    if bot_choice == 'rock':
        rock_choice += 1
    elif bot_choice == 'paper':
        paper_choice += 1
    else:
        scissors_choice += 1    
    intentos += 1

print(f'El bot eligio piedra {rock_choice} de veces')    
print(f'El bot eligio papel {paper_choice} de veces')    
print(f'El bot eligio tijeras {scissors_choice} de veces')    
"""    
    

    
    
    