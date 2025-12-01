"""
2) Realizar un programa que permita el intercambio de valores entre dos variables.
Por ejmplo: Si una variable numero vale 35, y una variable numero2 vale 20,
pase a valer 35. Una ves realizado el cambio a mostrar el resultado en la pantalla.
"""

n1 = 35
n2 = 20

print(f"\nn1 vale {n1} y n2 vale {n2}")

n1, n2 = n2, n1

print(f"\nn1 vale {n1} y n2 vale {n2}\n")