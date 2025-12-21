/*1. Haga un programa que tome dos numeros y pruebe cual es mayor*/

#include <iostream>

int main(void)
{
    int a;
    std::cout << "Digita el valor de a: ";
    std::cin >> a;

    int b;
    std::cout << "digita el valor de b: ";
    std::cin >> b;

    if (a > b)
    {
        std::cout << "\na es mayor que b\n";
    }
    else if (a < b)
    {
        std::cout << "\nb es mayo que a\n";
    }
    else
    {
        std::cout << "\nambos son iguales\n";
    }
    return 0;
}