# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 08:33:47 2025

@author: alesa
"""

"""Modulo 2, Problema 4: Comprovacion de par o impar"""

n = int(input('Digite un número entero -> '))

if n == 0:
    print('El numero es cero')
elif n %2 == 0:
    print('El número es par')
else:
    print('El número es impar')