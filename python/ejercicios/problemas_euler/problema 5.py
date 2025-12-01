# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 11:41:34 2025

@author: alesa
"""


"""Smallest Multiple"""








    

    
# Definir la lista de números
numeros = [16, 3, 5, 7, 9, 11, 13, 17, 19]

def mcd(a, b):
    """Calcula el máximo común divisor (mcd) usando el algoritmo de Euclides."""
    while b:
        a, b = b, a % b
    return a

def mcm(a, b):
    """Calcula el mínimo común múltiplo (mcm) usando el mcd."""
    # Usar la fórmula mcm(a,b) = (a * b) // mcd(a,b)
    return (a * b) // mcd(a, b)

# Inicializar el resultado con el primer número de la lista
resultado = numeros[0]

# Calcular el mcm de manera iterativa para todos los números de la lista
for i in range(1, len(numeros)):
    resultado = mcm(resultado, numeros[i])

print('El mínimo común múltiplo es:', resultado)
