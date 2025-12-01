# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 12:09:07 2025

@author: alesa
"""


"""Modulo 4, Problema 11: Vectores con listas"""


x = [1,2,3]
y = [-1,0,2]
xy = []

for i in range(len(x)):
    xy.append(x[i] * y[i])

    

print(f'Producto escalar: {xy[0] + xy[1] + xy[2]}')    