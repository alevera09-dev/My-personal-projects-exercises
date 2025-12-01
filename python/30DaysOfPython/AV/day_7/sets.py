# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 16:00:30 2025

@author: alesa
"""


"""
Day 7 - Sets/Conjuntos
"""


# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


"""
#Tamaño del set
print(len(it_companies))

#Agregar objetos a un set con .add
it_companies.add('Twitter')
print(it_companies)

it_companies.add('Nvidia'); it_companies.add('Intel'); it_companies.add('AMD')
print(it_companies)

#Diferencia entre .remove y .discard en sets
it_companies.remove('Google'); it_companies.discard('IBM')
print('\n', it_companies)

#si el objeto no existe .remove da error pero .discard no sino que lo ignora y sigue el programa
it_companies.discard('Sony')
print('\n', it_companies)
it_companies.remove('Samsung')
print('\n', it_companies)
"""

"""
#Union de conjuntos
C =  A.union(B)
print(C)

#Interseccion de conjuntos
print(A.intersection(B))

#Es subconjunto o subset de otro conjunto?
print(A.issubset(B))

#Esta desconectado un conjunto o set de otro?
print(A.isdisjoint(B))

#Cual es la diferencia simetrica de dos conjuntos o sets
print(A.symmetric_difference(B))

#Conjuntos/sets limpios con .clear
A.clear(); B.clear(); C.clear()
print(A, B, C)
"""


#Diferncia de tamaños de objetos entre sets y listas

#La lista con edades tiene 8 objetos
print(len(age))

#Mientras que este set tien 5 objetos
set_age = set(age)

#Explicacion: dato tipo list permite objetos repetidos, los sets no y los elimina al detectarlos
print(len(set_age))


explicacion_string = """Los strings son cara caracteres, 
solo funcionan para mostrarse mas no para calcular o otras cosas, es muy diferente un '10' a un 10"""


explicacion_list = ['Las listas son conjuntos que almacenan datos, son muy flexibles en sus funciones y en que se puede modificar o hacer con ella']
explicacion_tuple = ('Lo mismo que las listas pero las tuplas son inmutables, sus datos ya almacenados no pueden modificarse')

















