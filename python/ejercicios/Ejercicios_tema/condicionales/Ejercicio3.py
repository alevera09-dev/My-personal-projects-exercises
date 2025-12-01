# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 17:24:46 2025

@author: alesa
"""

"""Modulo 2, Problema 3: Comprobacion de 0 en una division"""

a = int(input('Digite un número -> '))
b = int(input('Digite otro número -> '))

if b == 0:
    print('No se puede dividir por 0')
else:
    print(f'{a} / {b} = {a / b}')