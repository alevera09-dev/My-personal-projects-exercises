# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 10:57:36 2025

@author: alesa
"""

"""
Day 8 - Diccionarios/Dictionary
"""

""" El tipo de dato de los diccionarios es dict """



dog = {
       'color' : 'Negro con blanco',
       'breed' : 'Cocker',
       'legs' : '',
       'age' : '1 año',
}


student_1065 = {
                'first_name' : 'Alejandro',
                'last_name' : 'Vera Lopez',
                'gender' : 'Male',
                'age' : 16,
                'marital_status' : False,
                'skills' : ['Newbie in python'],
                'country' : 'Colombia',
                'city' : 'Bucaramanga',
                'adress' : {
                            'street' : 'Hollow Street',
                            'zipcode' : '28853',
                    },
}



student_1065['skills'].append('Future programmer')


student_1065.pop('adress')
print(student_1065)
print(dog)

del dog

print(dog)
