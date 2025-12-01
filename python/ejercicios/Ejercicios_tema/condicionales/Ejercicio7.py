# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 10:54:20 2025

@author: alesa
"""

"""Modulo 2, Problema 7: Tipo impositivo"""


try:
    
    annual_rent = float(input('¿De cuanto es su renta anual? '))

except ValueError:
    print('\n\t|ERROR: Tu renta anual se debe escribir en numeros|')


if annual_rent <= 0:
    print('Su renta anual no puede ser negativa o 0')
elif annual_rent < 10_000:
    tipo = 5
elif annual_rent >= 10_000 and annual_rent < 20_000:
    tipo = 15
elif annual_rent >= 20_000 and annual_rent < 35_000:
    tipo = 20
elif annual_rent >= 35_000 and annual_rent < 60_000:
    tipo = 30
elif annual_rent >= 60_000:
    tipo = 45      
else:
    print('=/')       
    
    
print(f'Tienes que pagar {annual_rent * tipo/100}$')    