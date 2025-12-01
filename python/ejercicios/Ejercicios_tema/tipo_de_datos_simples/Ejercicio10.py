# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 15:58:04 2025

@author: alesa
"""

"""Modulo 1, Problema 10: Venta de juguetes"""

clown_weight, doll_weight = 112, 75 #gramos o g

clown_sold = int(input('¿Cuantos payasos se han vendido en el ultimo pedido? '))
doll_sold = int(input('¿Cuantas muñecas se han vendido en el ultimo pedido? '))
total_weight = (clown_sold * clown_weight) + (doll_sold * doll_weight)

print(f'El peso total de todo los juguetes vendidos son {total_weight}')
