# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 16:24:27 2025

@author: alesa
"""

"""Modulo 1, Problema 11: Cuenta de ahorros"""

actual_money = float(input('¿Cuanto dinero depositas en la cuenta? '))
year_one =  actual_money * 1.04
year_two = year_one * 1.04
year_three = year_two * 1.04

print(f'Primer año: {year_one:.2f}\nSegundo año: {year_two:.2f}\nTercero año: {year_three:.2f}')