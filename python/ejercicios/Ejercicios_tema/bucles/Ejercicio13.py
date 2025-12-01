# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 11:46:24 2025

@author: alesa
"""


"""Modulo 3, Problema 13: Eco infinito hasta qye el usuario decida"""

in_put = input('Escribe algo, si quieres sair escribe salir o exit >> ').lower()

while in_put != 'salir':
        
    print(in_put)
    in_put = input('Escribe algo, si quieres sair escribe salir o exit >> ').lower()
        
