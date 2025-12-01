# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 15:08:09 2025

@author: alesa
"""


"""Modulo 5, Problema 5: Asignaturas con diccionarios"""

asignaturas = {
               'Matemáticas': 6,
               'Física': 4,
               'Química': 5,
               }

total_puntos = 0
for i in asignaturas:
    print(f'{i} tiene {asignaturas[i]} créditos')
    total_puntos += asignaturas[i]
print(f'Total de puntos: {total_puntos}')    