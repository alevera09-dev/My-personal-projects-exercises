# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 17:30:09 2025

@author: alesa
"""


"""Modulo 4, Problema 6: asignaturas desaprobadas"""

nota_aprobatoria = 5
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []

for subject in subjects:
    score = float(input(f'¿Que notas has sacado en {subject}? '))
    if score < nota_aprobatoria:
        scores.append(subject)
        
print('Asignaturas que debes repetir:',scores)        