# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 11:45:22 2025

@author: alesa
"""

"""Modulo 4, Problema 9: Veces que se repite una vocal en una palabra"""

word = input('Escriba una palabra >> ').lower()
vocal = ['a','e','i','o','u']

for i in vocal:
    x = 0
    for j in word:
        if i == j:
            x += 1
    print(f'{i}: {x}')