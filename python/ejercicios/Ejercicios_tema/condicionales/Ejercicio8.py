# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 11:17:35 2025

@author: alesa
"""

"""Modulo 2, Problema 8: Comprobacion de desempeño en el trabajo"""


score = float(input('¿Cual es su puntuación? (0.0, 0.4, 0.6 o mas): '))

if score == 0.0:
    perfomance = 'Inaceptable'
    bonus = 2400 * score
    x = 1
elif score == 0.4:
    perfomance = 'Aceptable'
    bonus = 2400 * score
    x = 1
elif score >= 0.6:
    perfomance = 'Meritorio'
    bonus = 2400 * score
    x = 1
else:
    print('Pon una puntuacion valida')
    x = 0
 
if x:    
    print(f'Nivel de rendimiento: {perfomance}')
    print(f'Bonus: {bonus}$')   