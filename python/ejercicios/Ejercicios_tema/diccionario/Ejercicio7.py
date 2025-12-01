# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 08:54:53 2025

@author: alesa
"""


"""Modulo 5, Problema 7: Compras"""

total_compra = 0
canasta_compras = {}
salir = True

respuestas_correctas = ['1','2']

while salir:
    print('\n\n\t|Canasta De Compras Virtual|')
    print('\n/1: Añadir Articulo/') 
    print('/2: Salir/')
    opc = input('\n.:Opcion:. >> ')
    
    if opc in respuestas_correctas:
        
        if opc == '1':        
            producto = input('\n\nEscriba el articulo a añadir >> ').capitalize()
            precio = float(input('¿Cual es el precio de ese articulo? >> '))
            if precio <= 0:
                print('El precio del producto no puede ser 0 o negativo')
            else:
                canasta_compras[producto] = precio
        else:
            salir = False
            
    else:
        print('\n\nOpcion inexistente, elige bien la proxima|')
    
    
print('\n\nCanasta de compras: ')
for compras in canasta_compras:
    print(f'\n{compras}: {canasta_compras[compras]} $')
    total_compra += canasta_compras[compras]
    
print('Total de la compra: ', total_compra, '$')    
    