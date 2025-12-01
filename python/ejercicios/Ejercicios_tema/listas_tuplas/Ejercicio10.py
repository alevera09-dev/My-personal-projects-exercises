# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 12:04:36 2025

@author: alesa
"""


"""Modulo 4, Problema 10: Menor y mayor precio"""


prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
for price in prices:
    if price < min:
        min = price
    elif price > max:
        max = price 
print("El mínimo es " + str(min)) 
print("El máximo es " + str(max))


