# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 08:25:22 2025

@author: alesa
"""

#Suma de multiplos de 3 y 5
i = 0
ii = 0
suma = 0


while ii < 999:
    ii += 3
    if ii >= 10:
        while ii %3 != 0:
            ii -= 1
    
    if ii %3 == 0:
        suma += ii
    
while i < 995:
      i += 5
      if i >= 10:
          while i %5 != 0:
              ii -= 1
      
      if i %5 == 0:
          suma += i

    
def solution_naive() -> int:
    sum_of_multiples = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiples += i
    return sum_of_multiples
    


def solution_set() -> int:
    multiples_of_3 = {i * 3 for i in range(1, 999 // 3 + 1)}
    multiples_of_5 = {i * 5 for i in range(1, 999 // 5 + 1)}
    all_multiples = multiples_of_3 | multiples_of_5
    return sum(all_multiples)



def sum_of_natural_numbers(end: int, step: int) -> int:
    count = end // step + 1
    return count * (count - 1) * step // 2



def solution_closed_form() -> int:
    return (
        sum_of_natural_numbers(999, 3)
        + sum_of_natural_numbers(999, 5)
        - sum_of_natural_numbers(999, 15)
    )



print('Mi solucion: ', suma)
print('Solucion 1: ', solution_naive())
print('Solucion 2: ', solution_set())
print('Solucion 3: ', solution_closed_form())





