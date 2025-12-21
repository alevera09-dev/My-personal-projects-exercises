/*1. Escribe un programa que lea de la entrada estandar dos numeros y muestre 
en la salida estandar su suma, resta, multiplicacion y division. */

#include <iostream>

using namespace std;

int main(void)
{
    int number_1;
    cout << "Digita el valor de un numero: ";
    cin >> number_1;

    int number_2;
    cout << "Digita el valor de otro numero: ";
    cin >> number_2;

    cout << endl << number_1 << " + " << number_2 << " = " << number_1 + number_2 << endl;
    cout << number_1 << " - " << number_2 << " = " << number_1 - number_2 << endl;
    cout << number_1 << " * " << number_2 << " = " << number_1 * number_2 << endl;
    cout << number_1 << " / " << number_2 << " = " << number_1 / number_2 << endl;

    return 0;
}