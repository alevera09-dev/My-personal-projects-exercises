# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 10:35:08 2025

@author: alesa
"""

"""Modulo 3, Problema 8: Generador de Triángulos rectángulos pero ahora con números"""


h = int(input('Altura de el triángulo rectángulo >> '))

for i in range(h):
    for j in range(i+1):
        print(1+(2*i)-(2*j), end=' ')
    print("")


n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")
    