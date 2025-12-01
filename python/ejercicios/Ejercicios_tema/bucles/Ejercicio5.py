# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 09:31:24 2025

@author: alesa
"""

"""Modulo 3, Problema 5: Predecir dinero a ganar en inversión"""


amount_invest = float(input('¿Cuánto dinero invertiras? '))
annual_interest = float(input('¿De cuanto porcentaje es el interes anual? '))
years_investment = int(input('¿Cuantos años durará la inversión? '))
i = 1

print('=======================')
print('Prediccion de ganancias anual')
print('=======================')


while i <= years_investment:
    
    print(f'Año: {i}')
    gained_annual = amount_invest * (annual_interest/100)
    print(f'\tGanancia: {gained_annual:.2f}')
    amount_invest = amount_invest * (1 + annual_interest/100)
    print(f'\tDinero Actual: {amount_invest:.2f}')
    print('=======================')
    
    
    i += 1


print('\n\t|FIN DEL PROGRAMA|')    