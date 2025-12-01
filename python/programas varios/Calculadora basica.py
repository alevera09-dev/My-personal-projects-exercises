# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 15:38:50 2025

@author: alesa
"""

"""
Calculadora básica en terminal con python
"""

option = 'n'
int_float = True

#Titulo
print('\n\t\t\t\t|Calculadora Básica|')

if option == 'n':
    print('\n\n\t.:Que formato de salida quieres?, Entero o Decimal?, Actualmente esta en Entero para cambiarlo presiona D/d:.')
    int_float = True
    
elif option == 'd':
    print('\n\n\t.:Que formato de salida quieres?, Entero o Decimal?,'
          '\n\t  Actualmente esta en Decimal para cambiarlo presiona N/n:.')
    int_float = False
    
    
print('\n\t.:Hacer operaciones -> presiona C/c:.')

option = input('\n\n\t.:Que eliges? -> :.').lower()



if option == 'c':
    print('''|Ayuda: Primero digite un numero o mas ejemplo 5 o 237485,
          luego el signo de la operacion y finalmente el segundo numero o cantidad grande de numero|''')

    a = float(input(('\nHaga su operacion aqui -> ')))
    print(a)
    operacion = input('Operacion? -> ')
    print(a, operacion)
    b = float(input('-> '))
       
    if operacion == '+':
        print(f'{a} {operacion} {b} = {a+b}')
    elif operacion == '-':
        print(f'{a} {operacion} {b} = {a-b}')
    elif operacion == '*':
        print(f'{a} {operacion} {b} = {a*b}')
    elif operacion == '/':
        try:
            print(f'{a} {operacion} {b} = {a/b}')    
        except ZeroDivisionError:
            print('No se puede dividir por cero, vuelve a intentarlo!')
                               
                
                
                
                
                