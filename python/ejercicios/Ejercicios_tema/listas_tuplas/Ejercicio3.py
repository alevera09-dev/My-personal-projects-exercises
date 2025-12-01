# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 12:07:55 2025

@author: alesa
"""

"""Modulo 4, Problema 3: Nota de asignaturas"""


subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])
