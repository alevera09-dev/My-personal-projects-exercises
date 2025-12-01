# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 18:37:00 2025

@author: alesa
"""

"""
Day 11 in 30 Day Of Pyhton - Funtions - Level 2.
"""


def even_and_odds(n):
    odd_number = n//2
    even_number = odd_number+1
    print(f"The number of odds are {odd_number}\nThe number of evens are {even_number}")
def factorial(n):
    product = 1
    
    for i in range(1,n+1):
        product *= i
    return product    
def is_empty(dato):
    dato = str(dato)
    if len(dato) < 1:
        return print('El parametro esta vacio!!!')
    if True:
        return print('Hay parametro')
def calculate_mean(array):
    mean = sum(array)/len(array)
    return round(mean)
def calculate_median(array:list):
    array.sort()
    if len(array) %2 == 0:
        median_index = (len(array) - 1)//2
        median = (array[median_index] + array[median_index+1])//2
        return median
    if True:
        median_index = (len(array) - 1)//2
        return array[median_index] 
def calculate_mode(array:list):
    # Crear un diccionario vacío para almacenar los conteos
    frecuencias = {}

    # Contar la frecuencia de cada número en la lista
    for numero in array:
        if numero in frecuencias:
            frecuencias[numero] += 1
        else:
            frecuencias[numero] = 1

    # Si la lista está vacía, no hay moda
    if not frecuencias:
        return []

    # Encontrar la frecuencia más alta
    max_frecuencia = 0
    for frecuencia in frecuencias.values():
        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia

    # Encontrar todos los números con la frecuencia más alta
    modas = []
    for numero, frecuencia in frecuencias.items():
        if frecuencia == max_frecuencia:
            modas.append(numero)

    # Devolver la lista de modas
    return modas
def calculate_range(array=list):
    return max(array) - min(array)
def calculate_variance(array=list):
    median = calculate_median(array)    
    list_aux = []
    
    for number in array:
        list_aux.append((number - median)**2)
    
    return sum(list_aux)/len(list_aux)    
def calculate_std(array=list):
    from math import sqrt
    variance = calculate_variance(array)
    return sqrt(variance)



ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
print(calculate_variance(ages))