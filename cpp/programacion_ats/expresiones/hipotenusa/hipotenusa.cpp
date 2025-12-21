/*8. Escriba un programa que lea de la entrada estandar los dos catetos de un triangulo rectangulo
y escriba en la salida estandar su hipotenusa*/

#include <iostream>
#include <cmath>

int main(void)
{
    double cateto_a;
    std::cout << "Digita el valor de cateto a: ";
    std::cin >> cateto_a;

    double cateto_b;
    std::cout << "Digita el valor de cateto b: ";
    std::cin >> cateto_b;
    
    float hipotenusa = sqrt((cateto_a * cateto_a) + (cateto_b * cateto_b));
    std::cout << "La hipotenusa es: " << hipotenusa << std::endl;
    return 0;
}