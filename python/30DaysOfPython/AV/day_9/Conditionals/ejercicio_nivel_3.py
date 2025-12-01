# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 10:56:19 2025

@author: alesa
"""

"""
30Days Of Python - Conditionals, Level 3
"""


alevera = {
    'first_name' : 'Alejandro',
    'last_name' : 'Vera Lopez',
    'gender' : 'Male',
    'age' : 16,
    'marital_status' : False,
    'skills' : ['python'],
    'country' : 'Colombia',
    'city' : 'Bucaramanga',
    'adress' : {
        'street' : 'Hollow Street',
        'zipcode' : '28853',
}
}


if 'skills' in alevera.keys() and 'python' in alevera['skills']:
    print('Sabe de python')
else:
    print('\_(-_-)_/')