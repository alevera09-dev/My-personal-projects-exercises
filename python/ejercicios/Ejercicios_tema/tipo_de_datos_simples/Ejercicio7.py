# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 11:29:22 2025

@author: alesa
"""

"""Modulo 1, Problema 7: IMC(Indice de Masa Corporal)"""

peso = float(input('Tu peso en kg -> '))
estatura = float(input('Tu estatura en metros -> '))
imc = peso / estatura**2
print(f'Tu índice de masa corporal es {imc:.2f}')