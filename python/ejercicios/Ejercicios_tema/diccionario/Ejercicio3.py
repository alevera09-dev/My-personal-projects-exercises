# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 14:13:12 2025

@author: alesa
"""


"""Modulo 5, Problema 3: Precios de frutas"""


prices = {
          'Platano':1.35,
          'Manzana':0.80,
          'Pera':0.85,
          'Naranja':0.70,
}


fruit = input('Elige una fruta[Platano-Manzana-Pera-Naranja] >> ').capitalize()
kilo = float(input('¿Cuantos kilos qieres comprar? >> '))

if fruit in prices:
    print(f'\nTotal a pagar: {kilo * prices[fruit]}')
else:
    print('Esa fruta no esta disponible o lo que escribiste no tiene sentido')