# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 10:10:53 2025

@author: alesa
"""


def cuadrado_de_suma(n):
    a = 0
    for i in range(1, n+1):
        i, a = i + i, a + i
    return a ** 2


def suma_de_cuadrados(n):
    a = 0
    for i in range(1, n+1):
        i, a = i + i, a + i ** 2
    return a
       
#Resta

print(cuadrado_de_suma(1000) - suma_de_cuadrados(1000))   