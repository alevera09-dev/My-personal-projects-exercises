"""
Aplicacion que comprueba si el numero es par o impar
"""
"""
Lo necesario:
* Que el usuario pueda comprobar numeros hasta que quiera salir - completado
* Mostrar numeros primos hasta n - completado
* Mostrar Historial
"""
import pryme

#Menu principal
def main_menu():
    bandera_de_bucle = False
      
    print("\n_/** Pryme **\_")
    print("\nDigita cualquier numero entero y deja a la maquina comprobar si es primo o no a alta velocida =).")
    
    while True:
        repeats = 0
        
        if bandera_de_bucle:
            break
                    
        n = int(input("Digita un numero > "))
        
        print(f"\nEl numero {n} es", pryme.is_prime(n))
        pryme.historial(n, pryme.is_prime(n), "saved")
        
        
        while True:
            
            if repeats < 1:
                print("\n1. Evaluar otro numero.")
                print("2. Ver historial")
                print(f"3. Mostrar todo numero primo de 2 hasta {n}")
                print("4. Salir.")
            else:
                print("\n1. Evaluar otro numero.")
                print("2. Ver historial")
                print("3. Salir.")
                
            opc = input("\n>> ")


            if repeats < 1:
                if opc == "1":
                    bandera_de_bucle = False
                    break
                elif opc == "2":
                    print("\nHistorial:\n")
                    pryme.historial(operation="show")
                    pass
                elif opc == "3":
                    pryme.all_primes(n)
                    repeats = 1
                    bandera_de_bucle = False
                elif opc == "4":
                    print("Gracias por usar el programa, saliendo...")
                    bandera_de_bucle = True
                    break 
                else:
                    print("Opcion inexistente, vuelve a intentarlo.")    
            
            
            else:
                if opc == "1":
                    bandera_de_bucle = False
                    break
                elif opc == "2":
                    print("\nHistorial:\n")
                    pryme.historial(operation="show")
                    pass
                elif opc == "3":
                    print("Gracias por usar el programa, saliendo...")
                    bandera_de_bucle = True
                    break 
                else:
                    print("Opcion inexistente, vuelve a intentarlo.")


if __name__ == "__main__":
    main_menu()