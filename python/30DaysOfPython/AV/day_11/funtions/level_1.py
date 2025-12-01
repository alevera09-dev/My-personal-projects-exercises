# -*- coding: utf-8 -*-
"""
Day 11 in 30 Day Of Pyhton - Funtions - Level 1.
"""



def addition(a,b):
    return a + b
def area(r):
    import math
    return math.pi * r**2
def additions(*numbers):
    try:
        return sum(numbers)
    except TypeError:
        print('Error: Tipo de dato no soportado por la funcion add_all_numbers(), la funcion permite int o float')
def fahrenheit(celcius):
    """
    Pide un argumento de grados celcius y retorna su equivalente a farenheit
    
    Si el argumento dado no es valido retorna error
    
    Types validos: 'int' and 'float'
    """
    f = (celcius * 9/5) + 32
    return f
def season(month):
    """
    Pide un mes como argumento y retorna una estacion del año
    
    Si el argumento dado no es un mes retorna un error
    
    Types validos: 'str'
    """
    
    lista_meses = [
        ['diciembre','enero','febrero'],
        ['marzo', 'abril', 'mayo'],
        ['junio', 'julio', 'agosto'],
        ['septiembre', 'octubre', 'noviembre']           
]
    
    month = month.lower()
    if month in lista_meses[0]:
        return 'Invierno'
    if month in lista_meses[1]:
        return 'Primavera'
    if month in lista_meses[2]:
        return 'Verano'
    if month in lista_meses[3]:
        return 'Otoño'
    else:
        return 'Error: argumento no valido, esta funcion necesita un mes correcto'   
def slope(x1,y1,x2,y2):

    slope = (y2-y1) / (x2-x1)

    print(f'La distancia Euclidiana: {slope}')
def print_list(lista):
    for objeto in lista:
        print(objeto)
def reverse_list(lista):
    reversed_list = []
    for indice in range(len(lista)):
        reversed_list.insert(0, lista[indice])
    return reversed_list    
def capitalize_list_items(lista):
    capitalize_list = []
    for objeto in lista:
        capitalize_list.append(objeto.capitalize())
    return print(capitalize_list)    
def add_item(lista,item):
    lista.append(item)
    return print(lista)        
def remove_item(lista,item):
    lista.append(item)
    return print(lista)    
def sum_numbers(n):
    suma = 0
    for n in range(1, n+1):
        suma += n
    return suma    
def sum_of_odds(n):
    suma = 0
    for i in range(1,n+1,2):
        suma += i
    return suma    
def sum_of_even(n):
    suma = 0
    for i in range(0,n+1,2):
        suma += i
    return suma  
    
    
    



 
   





      