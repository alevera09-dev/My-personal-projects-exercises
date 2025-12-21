/*3. Realice un programa que lea un valor entero y determine si se trata de un
numero par o impar.*/

#include <iostream>

int main(void)
{
    int number;
    std::cout << "Digita un numero: ";
    std::cin >> number;

    if (number == 0)
    {
        std::cout << "\nEl numero es cero\n";
    }
    else if (number % 2 == 0)
    {
        std::cout << "\nEl numero es par\n";
    }
    else
    {
        std::cout << "\nEl numero es impar\n";
    }
    
    return 0;
}