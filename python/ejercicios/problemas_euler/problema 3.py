# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 15:16:18 2025

@author: alesa
"""


"""
Factores primos
"""


#Variables iniciales
division_completa = False #La factorizacion de numeros primos esta completa?
divisible = False #El numero es divisible?
i = 2 #Numero divisor
n = 725760 #Numero a factorizar


#Bucle que terminara cuando n/Numero sea 1 y de por terminado la factorizacion de forma exitosa
while division_completa == False:
      
    
    #Es n divisible por si? si lo es se divide
    if n %i == 0:
        n /= i
        divisible = True        
        print(i)
    
    #si no lo es se buscara un numero que si sea divisible
    else:
        
        #este bucle busca ese numero sumando de uno en uno  y comprobando si es divisible por n
        while n %i != 0:            
            i += 1
            divisible = False            
       
    
    #n es 1? si es asi dara la factorizacion exitosa como True
    if n == 1:        
        division_completa = True        
    
    #si no la factorizacion exirosa seguira siendo false y el bucle continuara
    else:        
        division_completa = False
        
        
        
        
#Si llegamos a aqui es que todo fue exitoso y imprimiremos el fin del programa       
print('\nFin del programa')



