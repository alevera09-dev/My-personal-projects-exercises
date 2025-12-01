# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 12:52:25 2025

@author: alesa
"""

"""Modulo 2, Problema 2: Años cumplidos con bucles"""

age = int(input('Digita tu edad -> '))

for i in range(age):
    i += 1
    
    if i == 1:
        print(f'Has cumplido {i} Año')
    else:
        print(f'Has cumplido {i} Años')
    