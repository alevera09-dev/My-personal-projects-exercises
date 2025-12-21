/*4. Comprobar si el numero digitado es positivo o negativo*/

#include <iostream>

int main(void)
{
    int number;
    std::cout << "Digita un numero: ";
    std::cin >> number;

    if (number > 0)
    {
        std::cout << "\nEl numero es positivo\n";
    }
    else if (number < 0)
    {
        std::cout << "\nEl numero es negativo\n";
    }
    else
    {
        std::cout << "\nEl numero es cero\n";
    }
    return 0;
}