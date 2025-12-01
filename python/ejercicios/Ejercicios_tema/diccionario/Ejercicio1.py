# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 12:30:45 2025

@author: alesa
"""

"""Modulo 5, Problema 1: Divisas"""


divisa = {
          'Euro':'€',
          'Dollar':'$',
          'Yen':'¥'
}

question = input('¿Cual es tu divisa? ').capitalize()

if question in divisa:
    print('EL simbolo de la divisa es:', divisa[question])
else:
    print('Esa divisa no existe en nuestra base de datos')