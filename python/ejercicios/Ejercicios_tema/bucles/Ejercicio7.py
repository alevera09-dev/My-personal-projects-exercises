# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 10:25:34 2025

@author: alesa
"""

"""Modulo 3, Problema 7: Tabla de multiplicar"""
"""
n = int(input('Elija el numero e la tabla de multiplicar >> '))
i = 1

while i <= 10:
    print(f'{n} * {i} = {n*i}')
    i += 1
"""    
    
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print('')    
