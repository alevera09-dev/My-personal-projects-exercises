# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 12:40:47 2025

@author: alesa
"""

"""Modulo 5, Problema 2: Guardado de datos"""


person = {
          'nombre':input('¿Cual es su nombre?: ').capitalize(),
          'edad':int(input('¿Cuantos años tienes?: ')),
          'direccion':input('¿Cual es tu direccion?: '),
          'telefono':input('¿Cual es tu telefono?: '),
}

print(f"{person['nombre']} tiene {person['edad']} años, vive en {person['direccion']} y su número telefonico es {person['telefono']}")