# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 08:10:22 2025

@author: alesa
"""

"""
Day 3 in 30DaysOfPython - Operadores
"""


"""
edad = 16
altura = 1.60
n_complex = (1+0j)

#algorithm area triangle

base = int(input('Digite la base de el triangulo -> '))
height = int(input('Digite la altura de el triangulo -> '))
area_of_triangle = 0.5 * base * height
"""


"""
# algorithm perimeter triangle

side_a = int(input('Enter side a -> '))
side_b = int(input('Enter side b -> '))
side_c = int(input('Enter side c -> '))
perimeter_triangle = side_a + side_b + side_c

print(f'The perimeter of the triangle is: {perimeter_triangle}')
"""


"""
# algorithm area and perimeter rectangle
legth = int(input('Digita la longitud -> '))
width = int(input('Digite el el ancho -> '))
perimeter_rectangle = 2 * (legth + width)
area_rectangle = legth * width
print(f'El area es: {area_rectangle}')
print(f'El perimetro es: {perimeter_rectangle}')
"""

"""
# algorithm circumference and area circle
r = int(input('Digite el radio -> '))
pi = 3.1416
area = pi * r ** 2
circumference = 2 * pi * r

print(f'El area del circulo es: {area}')
print(f'La circunferencia del circulo es: {circumference}')
"""


"""
#Algorithm calculacion de pendiente, interseccion de x y y de la y = 2x -2

#Formula y = mx - b donde m es la pendiente y b es la interseccion y

m, b, x, y = 2, -2, 0, -2 #y es igual que b pero solo la necesitamos para la operacion de x

if b > 0:
    y += (y * 2)
    x -= y
    x /= m
elif b < 0:
    y -= (y * 2)
    x += y
    x /= m
    
      
print(f'La pendiente es: {m}')
print(f'La interseccion de x es: {x}')
print(f'La interseccion de y es: {b}')    
"""



"""
#Distancia Euclidiana / Euclidien Distance

x1,y1,x2,y2 = 2,2,6,10
Euclidien = (y2-y1) / (x2-x1)

print(f'La distancia Euclidiana: {Euclidien}')
"""


"""
print(len('dragon') < len('python'))

if 'on' in 'python' and 'dragon':
    print(True)
else:
    print(False)
    
if 'jargon' in 'I hope this course is not full of jargon':
    print(True)
else:
    print(False)

if not 'on' in 'python' and 'dragon':
    print(True)
else:
    print(False)

        
test = str(float(len('python')))
print(test)
"""


"""
#Comprobador de numero par o impar

n1 = 3
n2 = 2

if n1 %2 == 0:
    print(f'numero {n1} es par')
else:
    print(f'numero {n1} es impar')

if n2 %2 == 0:
    print(f'numero{n2} es par')
else:
    print(f'numero {n2} es impar')    
"""


"""
a = 7 // 3
b = int(2.7)

print(a == b)

print('10' == 10)
print(int(9.8))
"""


"""
#Salario por hora
hours = int(input('Cuantas horas de trabajo -> '))
rate = int(input('Cuanto ganas a la hora -> '))

print(rate * hours)

#Cuantos segundos has vivido segun tus años

years = int(input('Cuantos años tienes? -> '))
seconds = years * 31557600

print(f'Has vivido {seconds} segundos')
"""


"""
i = 0
ii = 1
while i < 5:
    print(ii ** 3)
    i +=1
    ii += 1
"""







