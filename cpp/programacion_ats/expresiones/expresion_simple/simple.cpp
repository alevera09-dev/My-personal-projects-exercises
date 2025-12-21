//1. Escribe la siguiente expresion como expresion en C++, a/b + 1

#include <iostream>

using namespace std;

int main(void)
{
    float a;
    cout << "Digita el valor de a: ";
    cin >> a;

    float b;
    cout << "Digita el valor de b: ";
    cin >> b;

    float expresion = (a/b) + 1;
    cout.precision(2);
    cout << "\nEl resultado es: " << expresion << endl;

    return 0;
}