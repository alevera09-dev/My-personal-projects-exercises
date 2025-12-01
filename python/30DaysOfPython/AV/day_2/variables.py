"""
Day 2 in 30DaysOfPython
"""


"""
# variables y multi-variables en una linea
name, surname = 'Alejandro', 'Vera'
full_name = name + ' ' + surname
country, city, age, year = 'Colombia', 'Bucaramanga', 16, 2025
is_married, light_on, is_true = True, False, True


print(' Name: ', type(name),'\n','Surname: ', type(surname),'\n',
      'Full Name: ',type(full_name),'\n','Country: ',type(country),'\n',
      'City: ',type(city),'\n','Age: ',type(age),'\n','Year: ',type(year),'\n',
      'Married: ',type(is_married),'\n','True: ', type(is_true),'\n',
      'Light On: ',type(light_on), '\n')

print(f'Cantidad de letras de mi nombre: {len(name)}',
      f'\nCantidad de letras de mi apellido: {len(surname)}')
"""


"""
a,b = 5,4
total, diff, product, division = a + b, b - a, b * a, a / b
remainder, exp, floor_division = b % a, a ** b, a // b

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)
"""


"""
import math as m

radius = float(input('Radio del circulo -> '))
area_of_circle = m.pi * radius ** 2
circum_of_circle = (2 * m.pi) * radius

print(f'Area of circle : {area_of_circle:.2f}',
      f'\ncircum of circle: {circum_of_circle:.2f}')
"""

name, surname = input('Cual es tu nombre? '), input('Cual es tu apellido? ')
country, age = input('Cual es tu pais? '), int(input('Cuantos años tienes? '))

print(f'\nName: {name}', f'\n Surname: {surname}', f'\nFullname: {name + ' ' + surname}',
      f'\nCountry: {country}', f'\nAge: {age}')




