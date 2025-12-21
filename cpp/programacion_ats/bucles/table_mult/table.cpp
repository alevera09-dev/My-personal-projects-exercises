/*1. Realie un programa que solicite de la entrada estandar un entero del 1 al 10
y muestre en la salida estandar su tabla de multiplicar.*/

#include <iostream>
#include <cstdio>

int main(void)
{
    int number;
    
    do
    {
        std::cout << "Digita un numero del 1 al 10: ";
        std::cin >> number;
    } while (number < 1 || number > 10);
    
    std::cout << std::endl;
    for (int i = 1; i <= 10; i++)
    {
        std::cout << number << " * " << i << " = " << number * i << std::endl;
    }
    
    return 0;
}