# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 11:36:51 2025

@author: alesa
"""

"""Modulo 2, Problema 9: Comprobacion de pago"""



try:
    client_age = int(input('¿Cual es la edad del cliente? '))

    if client_age > 0 and client_age < 100:
    
        if client_age < 4:
            print('Precio: Gratis')    
        elif client_age >= 4 and client_age <= 18:
            print('Precio: 5$')
        elif client_age > 18:
            print('Precio: 10$')
        else:
            print('=/')

    else:
        print('Tu edad no puede ser negativa, 0 o mayor de 100')

except ValueError:
    print('Tu edad claramente no puede ser un numero decimal ni letras')
finally:      
    print('\n\t|Programa terminado|')


