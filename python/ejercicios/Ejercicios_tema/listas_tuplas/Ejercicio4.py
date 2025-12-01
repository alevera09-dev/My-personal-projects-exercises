# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 12:09:50 2025

@author: alesa
"""

"""Modulo 4, Problema 4: ordenancia de numeros ganadores"""

numeros_ganadores = []
b = 5

while b:
    
    numeros_ganadores.append(int(input('Digite los numeros gandores')))
    b -= 1
    

numeros_ganadores.sort()   
print(numeros_ganadores)    


