# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 12:30:19 2025

@author: alesa
"""

"""Modulo 3, Problema 1: Bucle de strings"""

name = input('Digite su nombre: ')

for i in range(1,11):
    print('For: ', i, ':',  name)

print('\n')

i = 1 
while i < 11:
    
    print('While: ', i, ':', name)
    i += 1    