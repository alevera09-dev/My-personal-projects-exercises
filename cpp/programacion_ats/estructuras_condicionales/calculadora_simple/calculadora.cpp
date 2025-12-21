/*12.

Hacer un menu que considere las siguientes opciones:

    1. Cubo de un numero.
    2. Numero par o impar
    3. Salir
*/

#include <iostream>

int main(void)
{
    std::cout << "\tMINI_CALCULADORA EN C++\n";
    std::cout << "\n1. Cubo de un numero.";
    std::cout << "\n2. Numero par o impar.";
    std::cout << "\n3. Salir.";
    
    int opc;
    std::cout << "\n\n>> ";
    std::cin >> opc;

    int number;
    std::cout << "\n\nDigita un numero: ";
    std::cin >> number;

    if (opc == 1)
    {
        std::cout << "\n\nEl cubo de " << number << " es " << number*number << std::endl;
    }
    else if (opc == 2)
    {
        if (number % 2 == 0)
        {
            std::cout << "\n\nEl numero " << number << " es par.\n";
        }
        else
        {
            std::cout << "\n\nEl numero " << number << " es impar.\n";
        }
    }

    return 0;
}