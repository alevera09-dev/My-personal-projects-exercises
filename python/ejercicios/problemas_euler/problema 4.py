# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 16:19:40 2025

@author: alesa
"""


"""
Problema 4: Producto Palindromico
"""


operacion_resuelta = False
n = 0
mult1 = 999
mult2 = 999


while operacion_resuelta == False:
    
    n = mult1 * mult2
    n = str(n)
    
    if n[::-1] == n:
        operacion_resuelta = True
    else:
        n = int(n)
        mult2 -= 1
       
print(n)    
        
