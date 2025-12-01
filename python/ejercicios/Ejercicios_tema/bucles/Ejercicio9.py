# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 11:00:38 2025

@author: alesa
"""

"""Modulo 3, Problema 9: Comprobacion de contraseña"""

password_saved = 'Alevera09'
password = input('Digite su contraseña >> ')
incorrect = 0
while password != password_saved:
    
    incorrect += 1
    print('\nIncorrecto')
    
    if incorrect == 1:
        password = input('\nDigite su contraseña correcta >> ')
    elif incorrect == 2:
        password = input('\nDigite su contraseña |CORRECTA| >>>>>>>>>> ')
    elif incorrect == 3:
        false_user = True
        break


if false_user == False:    
    print('\nCorrecto')
else:
    print('\n\n\t!Vete de aqui impostor!')    