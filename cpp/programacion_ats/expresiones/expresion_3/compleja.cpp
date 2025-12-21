//3. Escribe la siguiente expresion como si fuera de C++

#include <iostream>

int main(void)
{
    float a;
    std::cout << "Digita el valor de a: ";
    std::cin >> a;

    float b;
    std::cout << "Digita el valor de b: ";
    std::cin >> b;

    float c;
    std::cout << "Digita el valor de c: ";
    std::cin >> c;

    float d;
    std::cout << "Digita el valor de d: ";
    std::cin >> d;

    float e;
    std::cout << "Digita el valor de e: ";
    std::cin >> e;

    float f;
    std::cout << "Digita el valor de f: ";
    std::cin >> f;

    float expresion = (a + (b / c)) / (d + (e / f));
    std::cout.precision(3);
    std::cout << "\nResultado: " << expresion << std::endl;

    return 0;
}