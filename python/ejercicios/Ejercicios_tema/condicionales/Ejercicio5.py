# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 08:39:25 2025

@author: alesa
"""

"""Modulo 2, Problema 5: Comprobacion tributaria"""



#Codigo principal
try:

    #Variables iniciales, edad, salario mensual y si puede tributar o no
    age = int(input('¿Cual es tu edad? '))
    monthly_salary = float(input('¿Cuanto son tus ingresos mensuales? '))


    #Comprobacion si la edad no es falsa
    if age > 0 and age < 100:
        
        #Comprobacion si se puede tributar
        if age > 16 and monthly_salary >= 1000:
            print('\n¿Tienes que tributar?: SI')
        else:
            print('\n¿Tienes que tributar?: NO')
                    
    else:
        print('Tu edad no puede ser negativa, mayor de 100 o 0')

except ValueError:
    print('ERROR: recuerda que solo se permiten números y solo enteros en la edad =)')

finally:      
    print('\n\nPrograma terminado')    


