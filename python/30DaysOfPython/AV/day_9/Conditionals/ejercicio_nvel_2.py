# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 10:02:13 2025

@author: alesa
"""

"""
30Days Of Python - Conditionals, Level 2
"""

"""
score = int(input('¿Cual es tu puntuacion? >> '))

if score >= 0 and score <= 100:
    print('Tu calificacion es de:',end=' ')
    if score >= 0 and score <= 49:
        print('F')
    elif score >= 50 and score <= 59:
        print('D')
    elif score >= 60 and score <= 69:
        print('C')
    elif score >= 70 and score <= 89:
        print('B')
    elif score >= 90 and score <= 100:
        print('A')    
else:
    print('Esa puntuacion es invalida, razon: negativa o mayor a la maxima puntuacion')
"""

"""
months = input('Ingrese el nombre de un mes >> ').lower()

print('El mes corresponde a la estacion de', end=' ')
match months:
    case 'diciembre' | 'enero' | 'febrero':
        print('Invierno')
    case 'marzo' | 'abril' | 'mayo':
        print('Primavera')
    case 'junio' | 'julio' | 'agosto':
        print('Verano')
    case 'septiembre' | 'octubre' | 'noviembre':
        print('Otoño')
    case _:
        print('ninguna porque ese mes no existe =/')
"""

"""
fruits_list = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Escribe una fruta >> ').lower()

if fruit in fruits_list:
    print('Esa fruta ya esta en la lista')
else:
    fruits_list.append(fruit)
    print(fruits_list)
"""









