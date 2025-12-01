# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 17:01:06 2025

@author: alesa
"""

"""Modulo 2, Problema 1: comprobacion de edad"""


try:
    age = int(input('¿Cuantos años tienes? '))

    if age > 0 and age < 100:
    
        if age >= 18:
            print('Eres un adulto')    
        else:
            print('Eres un menor de edad')

    else:
        print('Tu edad no puede ser negativa o mayor de 100')

except ValueError:
    print('Tu edad claramente no puede ser un numero decimal')
finally:      
    print('\n\nPrograma terminado')