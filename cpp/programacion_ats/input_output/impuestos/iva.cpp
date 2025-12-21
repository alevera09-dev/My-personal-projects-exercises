/*2. Escribe un programa que lea de la entrada estandar el precio
de un producto y muestr en la salida estandar el precio del producto al aplicarle el IVA*/

#include <iostream>

using namespace std;

int main(void)
{
    float price;
    cout << "Digita el precio de su producto: ";
    cin >> price;

    cout << "El precio total con IVA es " << price * 1.19 << endl;

    return 0;
}