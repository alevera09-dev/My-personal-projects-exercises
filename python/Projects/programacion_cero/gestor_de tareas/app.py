# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 10:20:44 2025

@author: alesa
"""

"""Modulo: app"""

import funciones as fn
    


# Bucle indeterminado
while True:

    """
    * Menu de opciones - Output, Terminado
    * Logica de opciones 
    """

    #Menu de opciones - Output
    print('\n')
    print('='*40)
    print('Gestor De Tareas by Alevera'.center(38), '|')
    print('='*40)

    #Opciones(string)
    print('1.Añadir tareas', ' '*22, '|')
    print('2.Ver tareas', ' '*25,'|')
    print('3.Completar tareas', ' '*19, '|')
    print('4.Eliminar tareas', ' '*20, '|')
    print('5.Salir del programa', ' '*17, '|')
    print('='*40)
    
    #Input de opciones
    opc = input('\n\nQue opcion eliges > ')
    print('\n')
    
    #Menu de opciones
    if opc in ['1','2','3','4']:
        fn.options(opc)
    elif opc == '5':
        print('\nGracias por usar el programa, terminando...')
        break
    elif True:
        print('opcion invalida')






