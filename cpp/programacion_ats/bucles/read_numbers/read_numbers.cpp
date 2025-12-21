/*2. Realice un programa que lea de la entrada estandar numeros hasta que se introduzca un cero.
En ese momento el programa debe terminar y mostrar en la salida estandar el numero de valores
mayores que cero leidos.*/

#include <iostream>

int main(void)
{
    int number, i = 0;
    do
    {
        std::cout << "Introduzca un numero: ";
        std::cin >> number;

        if (number > 0)
        {
            i++;
        }

    } while (number != 0);
    
    std::cout << "\nLa cantidad de numeros ingresados mayor a cero es: " << i << std::endl;
    return 0;
}