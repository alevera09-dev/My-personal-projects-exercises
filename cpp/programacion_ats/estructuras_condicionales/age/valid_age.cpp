/*7. Escriba un programa que solicite una edad (un entero) e indique en la
salida estandar si la edad introducida esta en el rango [18-25]*/

#include <iostream>

int main(void)
{
    int age;
    std::cout << "Digita un numero: ";
    std::cin >> age;

    if (age >= 18 && age <= 25)
    {
        std::cout << "\nLa edad esta en el rango de 18-25\n";
    }
    else
    {
        std::cout << "\nLa edad no esta en el rango de 18-25\n";
    }

    return 0;
}