/*11. Hacer un programa que simule un cajero automatico con un saldo inicial
de 1000 Dolares.*/

#include <iostream>

int main(void)
{
    float saldo = 1000.0;

    std::cout << "\tCAJERO AUTOMATICO EN C++\n";
    std::cout << "\n1.Ingresar.";
    std::cout << "\n2.Retirar.";
    std::cout << "\n3.Ver saldo.";
    std::cout << "\n4.Salir.\n";

    int opc;
    std::cout << "\nDigita una opcion: ";
    std::cin >> opc;

    std::cout << std::endl;
    if (opc == 1)
    {
        float ingreso;
        std::cout << "Cuanto quieres ingresar: ";
        std::cin >> ingreso;

        if (ingreso < 0)
        {
            std::cout << "Ingreso invalido, no puede ser negativo.";
        }
        else
        {
            saldo += ingreso;
            std::cout << "Ingreso exitoso, ahora tienes " << saldo;
        }
    }
    else if (opc == 2)
    {
        float retiro;
        std::cout << "Cuanto quieres retirar: ";
        std::cin >> retiro;

        if (retiro < 0)
        {
            std::cout << "Retiro invalido no puede ser un numero negativo.";
        }
        else if (retiro > saldo)
        {
            std::cout << "Retiro invalido no puede ser mayor que el saldo.";
        }
        else
        {
            saldo += -retiro;
            std::cout << "Retiro exitoso, ahora tienes " << saldo;
        }
    }
    else if(opc == 3)
    {
        std::cout << "El saldo total: " << saldo;
    }
    std::cout << std::endl;

    return 0;
}