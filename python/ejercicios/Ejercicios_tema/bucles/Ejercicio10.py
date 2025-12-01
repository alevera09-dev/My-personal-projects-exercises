# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 11:20:19 2025

@author: alesa
"""


"""Modulo 3, Problema 10: Primo o no? con bucles"""


n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")