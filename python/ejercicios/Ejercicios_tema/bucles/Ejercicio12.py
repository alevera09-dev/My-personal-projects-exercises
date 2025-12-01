# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 11:32:05 2025

@author: alesa
"""

"""Modulo 3, Problema 12: Numero de letras en una palabra con bucles"""


word = input('Digite una palabra >> ').lower()
letter = input('Digite una letra >> ').lower()
repeats = 0

for i in range(len(word)):
    if letter == word[i]:
        repeats += 1
    else:
        continue

print(f'La letra {letter} se repite {repeats} veces en la palabra {word}')    