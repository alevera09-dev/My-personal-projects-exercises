# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 10:56:17 2025

@author: alesa
"""

"""Modulo: Funciones"""

"""
*Añadir tareas - completada
*Ver tareas - completado
*Completar tareas - mas o menos
*Eliminar tareas completado
*Otros componentes Lista(objetos list) - Creada
"""

#Lista de tareas
lista_de_tareas = []

#funciones del programa
def task_add(lista):
    task = input('Tarea a añadir >> ').capitalize()
    lista.append(task)
    print('***La tarea ha sido añadida con exito!***')
    print(f'***Se ha añadido la tarea de {lista[-1]}***')
    print('***Añadido como tarea numero***', len(lista))


def task_see(lista):
    #Condicional que evalue si algo esta en la lista
    if len(lista) > 0:
        #si hay algo en la lista se presenta
        print('\n')
        
        print('='*18)
        print('|Lista de Tareas |')
        
            
        for i in range(len(lista)):    
            print('='*60)
            print(f'|{i+1}| {lista[i]}', ' '*(57-len(f'|{i+1}| {lista[i]}')), '|')
            print('='*60)
            
    #si esta vacia avisa de ello
    else:
        print('\nNo hay tareas pendientes\n')
        
    #mensaje de fin de listado
    print('Fin de listado')


def task_complete(lista):
    #llamar a la funcion task_see()
    task_see(lista_de_tareas)
    
    #Entrada para que el usuario introduzca una tarea
    comp = int(input('Que lista desea marcar como completa? > '))

    #logica condicional para completar tareas
    if comp > 0 and comp <= len(lista):
        
        if '(Completada)' in lista[comp - 1]:
            print('La tarea ya esta completada')
        else:
            lista[comp-1] = lista[comp-1] + '(Completado)'
    else:
        print('Opcion no valida')
        
    
def task_delete(lista):
    task_see(lista_de_tareas)
    delete = int(input('\n\nQue tarea desea eliminar? > '))
    lista.pop(delete-1)
    task_see(lista_de_tareas)


def options(opc= str):    
    if opc == '1':
        return task_add(lista_de_tareas)
    if opc == '2':
        return task_see(lista_de_tareas)
    if opc == '3':
        return task_complete(lista_de_tareas)
    if opc == '4':
        return task_delete(lista_de_tareas)   
    
    
    
    str
    
    