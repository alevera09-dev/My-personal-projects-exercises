# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 14:26:48 2025

@author: alesa
"""


"""Modulo 5, Problema 4: Meses"""


months = {
           1:'Enero',
           2:'Febrero',
           3:'Marzo',
           4:'Abril',
           5:'Mayo',
           6:'Junio',
           7:'Julio',
           8:'Agosto',
           9:'Septiembre',
           10:'Octubre',
           11:'Noviembre',
           12:'Diciembre',
           'limit_days': {
                          'Enero':31,
                          'Febrero':28,
                          'Marzo':31,
                          'Abril':30,
                          'Mayo':31,
                          'Junio':30,
                          'Julio':31,
                          'Agosto':31,
                          'Septiembre':30,
                          'Octubre':31,
                          'Noviembre':30,
                          'Diciembre':31,
                          }
          }


print('¿Cual es la fecha?, utiliza el formato dd/mm/aaaa')
d = int(input('dd: '))
m = int(input('mm: '))
a = int(input('aaaa: '))    


if m in months:
    if d > 0 and d <= months['limit_days'][months[m]]:
        print(f'Fecha registrada: {d}/{months[m]}/{a}')
    else:
        print('Este numero de dia no existe')
    

else:
    print('este mes no existe')
    
    
    
    
meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')
print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])
    
    
    

