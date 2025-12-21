/*2. Haz un programa que tome tres numeros y compruebe cual es mayor.*/

#include <iostream>

int main(void)
{
    int a;
    std::cout << "Digita el valor de a: ";
    std::cin >> a;

    int b;
    std::cout << "Digita el valor de b: ";
    std::cin >> b;

    int c;
    std::cout << "Digita el valor de c: ";
    std::cin >> c;

    if (a > b && a > c)
    {
        std::cout << "\na es mayor\n";
    }
    else if (b > a && b > c)
    {
        std::cout << "\nb es mayor\n";
    }
    else if (c > a && c > b)
    {
        std::cout << "\nc es mayor\n";
    }
    else
    {
        std::cout << "\nson iguales\n";
    }

    return 0;
}