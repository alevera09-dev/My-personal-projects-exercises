# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 16:42:04 2025

@author: alesa
"""

"""Modulo 1, Problema 12: Panaderia"""

#Descuento
price = 3.49
discount = price * (1 - 0.6)

#Cantidad de barras vendidas
bread_sold = int(input('¿Cuantas barras de pan se han vendido hoy? '))

#mprimir los resultados: costo habitual, total de ahorro y precio final de la compra
print(f'Costo habitual: {price}$')
print(f'EL descuento es: {0.6 * 100}%')
print(f'El total a pagar es: {bread_sold * discount:.2f}')
