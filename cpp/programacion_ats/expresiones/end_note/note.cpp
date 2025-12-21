/*Escriba un programa que lea la nota final de cuatro alumnos
y calcule la nota final media de los cuatro alumnos*/

#include <iostream>

int main(void)
{
    float nota_1;
    std::cout << "Digita la nota del primer alumno: ";
    std::cin >> nota_1;

    float nota_2;
    std::cout << "Digita la nota del segundo alumno: ";
    std::cin >> nota_2;

    float nota_3;
    std::cout << "Digita la nota del tercer alumno: ";
    std::cin >> nota_3;

    float nota_4;
    std::cout << "Digita la nota del cuarto alumno: ";
    std::cin >> nota_4;

    float nota_media = (nota_1 + nota_2 + nota_3 + nota_4) / 4;

    std::cout.precision(2);
    std::cout << "La nota media es: " << nota_media << std::endl;
    
    return 0;
}