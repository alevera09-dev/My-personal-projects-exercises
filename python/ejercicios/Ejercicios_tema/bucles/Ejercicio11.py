# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 11:22:55 2025

@author: alesa
"""


"""Modulo 3, Problema 11: bucle de letras invertidas de una palabra"""


word = input('Digite una palabra >> ').lower()

for i in range(1,len(word)+1):
    print(word[-i], end='')
    
    