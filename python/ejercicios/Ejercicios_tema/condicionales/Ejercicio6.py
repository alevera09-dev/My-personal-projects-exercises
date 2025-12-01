# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 09:11:37 2025

@author: alesa
"""

"""Modulo 2, Problema 6: comprobacion de grupos"""


name = input('¿Cual es tu nombre? ').lower()
gender = input('¿Cual es tu genero?(Femenino/F o Masculino/M) ').lower()


"""
grupo a = mujeres con nombre < m y hombres con nombre > n - grupo b = el resto
"""


if ord(name[0]) >= 97 and ord(name[0]) <= 122:
   
    if (name[0] < 'm' and gender[0] == 'f') or (name[0] > 'n' and gender[0] == 'm'):
        print('esta en el Grupo A')
    else:
        print('esta en el Grupo B')
        
else:
    print('NOMBRE NO VALIDO!!!')
    
    
