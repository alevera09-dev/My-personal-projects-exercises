# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 12:38:09 2025

@author: alesa
"""

"""Modulo 3, Problema 3: Todos los números impares desde 1 hasta n, 1,3,5.....n"""

n = int(input('Digite un número positivo[Entero]-> '))

for i in range(n):
    i += 1
    if i %2 != 0:
        print(i, end=',')