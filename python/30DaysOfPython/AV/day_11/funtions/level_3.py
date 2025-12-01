# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 18:38:11 2025

@author: alesa
"""

"""
Day 11 in 30 Day Of Pyhton - Funtions - Level 3.
"""



def is_prime(n):
    """
    Revisa si en numero es primo.

    Args:
        number (int): The integer to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    from math import sqrt
    # Todo numero menor o igual a 1 no es primo.
    if n <= 1:
        return False
    
    # 2 es el unico numero par que es primo.
    if n == 2:
        return True
    
    # Todos los numeros pares no son primos.
    if n % 2 == 0:
        return False
    
    # Check for divisors from 3 up to the square root of the number.
    # Only need to check odd numbers, entonces incremento por 2.
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
            
    # Si no hay divisores son encontrados, el numero es primo.
    return True
def is_equal(array=list):
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

    if modas == array:
        return True
    if True:
        return False 
def is_array(lista_datos=list)  :
    """_summary_
    ¿Son todos los objetos de una lista del mismo tipo?

    Args:
        lista_datos (_list_): lista de cualquier con cualquier valor. Defaults to list.

    Returns:
        _bool_: 
        
            *si todos los objetos de la lista son del mismo tipo retorna True
            
            *de lo contrario retorna False
    """
    
    
    
    
    #la lista de datos es un array si sus datos son del mismo tipo
    equal = 0
    for i in range(1, len(lista_datos)):
        if type(lista_datos[i-1]) == type(lista_datos[i]):
            equal += 1
    
    if equal+1 == len(lista_datos):
        return True            
    
    #de lo contrario es una lista homogenea(datos de diferentes tipos) 
    if True:
        return False    
def is_valid_python_variable(name):    
    """
    Checks if a given string is a valid Python variable name.

    Args:
        name (str): The string to check.

    Returns:
        bool: True if the string is a valid Python variable name, False otherwise.
    """
    import keyword
    
    if not isinstance(name, str):
        return False  # Variable names must be strings

    # Check if it's a valid identifier according to Python's rules
    if not name.isidentifier():
        return False

    # Check if it's a Python keyword
    if keyword.iskeyword(name):
        return False

    return True
    
    
     
