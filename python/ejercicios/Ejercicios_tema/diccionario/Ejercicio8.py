# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 09:55:23 2025

@author: alesa
"""

"""Modulo 5, problema 8: Traduccuion con diccionarios"""


diccionario = {}
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(','):
    clave, valor = i.split(':')
    diccionario[clave] = valor
frase = input('Introduce una frase en español: ')
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')
        