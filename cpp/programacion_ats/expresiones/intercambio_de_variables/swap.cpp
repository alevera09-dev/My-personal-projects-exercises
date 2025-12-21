//5. escriba un fragmento de programa que intercambie los valores de dos variables.

#include <iostream>

int main(void)
{
    int a;
    std::cout << "Digita el valor de a: ";
    std::cin >> a;

    int b;
    std::cout << "Digita el valor de b: ";
    std::cin >> b;

    // Valores originales out
    std::cout << "\n--Valores Originales--\n";
    std::cout << "\na = " << a;
    std::cout << "\nb = " << b << std::endl;

    // Swap
    int aux = a;
    a = b;
    b = aux;

    // Nuevos Valores out
    std::cout << "\n--Nuevos Valores--\n";
    std::cout << "\na = " << a;
    std::cout << "\nb = " << b << std::endl;

    return 0;
}