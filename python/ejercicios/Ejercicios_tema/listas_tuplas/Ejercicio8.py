# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 10:53:37 2025

@author: alesa
"""


"""Modulo 4, Problema 8: Comprobación de palabra si es palindromo"""


word = input("Introduce una palabra: ").lower()
reversed_word = word
word_list = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()

if word_list == reversed_word:
    print(f'La palabra {word} es una palabra palíndroma')
else:
    print(f'La palabra {word} no es una palabra palíndroma')

