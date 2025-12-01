#Errores de python comunes, 30 Days Of Python, day 16

"""
#SintaxError
name = "Alejandro"
print name          #sintax incorrecto, print()


#NameError
print(apellido)     #name error, variable no definida

#TypeError
a = "a"
b = 5
c = a + b           #type error, a es str y b es int, no se puede sumar un str a un int

#IndexError
test_list = [1, 2, 3]
print(test_list[3])     #index error, no existe un indice de ese numero en la lista, el maximo indice es 2

#ModuleNotFoundError
import mahts            #modulo no existente, por ende no encontrado

#AttributeError
import math

PI = math.PI            #Attribute error, ya que el attribute no existe

#KeyError
test_dict = {
    "name": "Alejandro",
    "apellido": "Vera",
    
}

print(test_dict["edad"])        #Key Error, ya que la key no existe


#ImportError
from math import power      #Esta funcion o metodo no existe asi que no se puede importar por ende da un ImportError


#ZeroDivisionError
a = 5
b = 0
c = a / b       #No se puede dividir por cero asi que da error

#ValueError
variable = "12a"
variable_int = int(variable)        #ValueError ya que no se puede volver int el valor "12a" si fuera solo "12" no daria error

"""

