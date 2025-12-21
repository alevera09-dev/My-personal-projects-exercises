/*3. Realice un programa que calcule y muestre en la salida estandar la suma de los cuadrados de los 10 primeros enteros mayores a cero*/

#include <iostream>

int main(void)
{
    int suma = 0;

    for (int i = 1; i <= 10; i++)
    {
        suma += i*i;
    }

    std::cout << "La suma es: " << suma << std::endl;
    return 0;
}