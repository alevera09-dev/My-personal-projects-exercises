# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 15:18:51 2025

@author: alesa
"""


"""Modulo 5, Problema 6: Agregar objetos a un diccionarios"""


persona = {}
continuar = True

# Respuestas afirmativas que se aceptarán
respuestas_afirmativas = ['si', 's', 'y', 'yes']

while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    # Comprobar la respuesta del usuario de forma robusta
    respuesta = input('¿Quieres añadir más información (Si/No)? ').lower()
    continuar = respuesta in respuestas_afirmativas
