# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 12:13:41 2025

@author: alesa
"""

"""Modulo 2, Problema 10: Pizzeria"""


pizza = input('¿Quiere pizza vegetariana?[s/n]')

if pizza.lower() == 's':
    pizza = 'Vegetariana'
    print('====================')
    print('Ingredientes:')
    print('\nPimiento\nTofu')
    print('====================')
    

else:
    pizza = 'No Vegetariana'
    print('====================')
    print('Ingredientes:')
    print('\nPeperoni\nJamón\nSálmon')
    print('\nElige solo uno')
    print('====================')


ingrediente = input('\nElige solo uno -> ')

print('\n====================')
print(f'Eleccion: {pizza}')
print(f'Ingredientes: Mozarella - Tomate - {ingrediente.capitalize()}')
print('====================')    
