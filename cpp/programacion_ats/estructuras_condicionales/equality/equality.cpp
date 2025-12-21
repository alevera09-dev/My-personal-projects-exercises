/*8. Escribe un programa que lea de la entrada
estandar tres numeros. Despues debe leer
un cuarto numero e indicar si el numero coincide 
con algunos introducidos con anterioridad*/

#include <iostream>

int main(void)
{
    int numero_1;
    std::cout << "Digita un numero: ";
    std::cin >> numero_1;

    int numero_2;
    std::cout << "Digite un segundo numero: ";
    std::cin >> numero_2;

    int numero_3;
    std::cout << "Digite un tercer numero: ";
    std::cin >> numero_3;

    int numero_4;
    std::cout << "Digite un ultimo numero: ";
    std::cin >> numero_4;

    if (numero_4 == numero_1)
    {
        std::cout << "\nEl cuarto numero es igual al primer numero.\n";
    }
    else if (numero_4 == numero_2)
    {
        std::cout << "\nEl cuarto numero es igual al segundo numero.\n";
    }
    else if (numero_4 == numero_3)
    {
        std::cout << "\nEl cuarto numero es igual al tercer numero.\n";
    }
    else
    {
        std::cout << "\nEl cuarto numero es diferente a los demas numeros.\n";
    }

    return 0;
}