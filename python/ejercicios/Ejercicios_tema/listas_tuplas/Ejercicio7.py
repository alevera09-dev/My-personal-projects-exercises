# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 10:35:26 2025

@author: alesa
"""


"""Modulo 4, Problema 7: eliminacion de objeto que es multiplo de 3"""

abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
abc2 = []

for i in range(len(abc)):
    if (i+1) %3 != 0:
        abc2.append(abc[i])
        
print(abc2)
