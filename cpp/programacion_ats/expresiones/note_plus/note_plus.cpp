/*7. La calificacion final de un estudiante es la media ponderada de tres notras:

* La nota de practica que cuanta 30% del total,
* La nota teorica que cuenta un 60%
* La nota de participacion que cuanta con el 10% restante

Escriba un programa que lea de la entrada estandar las tres notas de un alumno y escriba en la
salida estandar su nota final
*/

#include <iostream>

int main(void)
{
    float nota_practica;
    std::cout << "Digita tu nota en practica: ";
    std::cin >> nota_practica;

    float nota_teorica;
    std::cout << "Digita tu nota en teoria: ";
    std::cin >> nota_teorica;

    float nota_participacion;
    std::cout << "Digita tu nota de participacion: ";
    std::cin >> nota_participacion;

    float nota_final = (nota_practica * 0.30) + 
                       (nota_teorica * 0.60) + 
                       (nota_participacion * 0.10);

    std::cout << "La nota final es: " << nota_final << std::endl;
    return 0;
}