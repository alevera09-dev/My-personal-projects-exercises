/*9. Realice un programa que calcule el valor que toma la siguiente funcion para
unos valores dados de x e y:

(sqrt(x)) / (y * y) - 1

*/

#include <iostream>
#include <cmath>

int main(void)
{
    double x;
    std::cout << "Digita el valor de x: ";
    std::cin >> x;

    double y;
    std::cout << "Digita el valor de y: ";
    std::cin >> y;

    float fn = (sqrt(x)) / (y * y) - 1;
    std::cout << "El resultado es: " << fn << std::endl;
    return 0;
}