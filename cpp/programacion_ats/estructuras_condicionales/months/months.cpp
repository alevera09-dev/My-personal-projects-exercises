/*10. Mostrar los meses del años, pidiendole al usuario un numero entre (1-12)
y mostrar el mes al que corresponde*/

#include <iostream>

int main(void)
{
    int months;
    std::cout << "Digita un valor en el rango de 1 a 12: ";
    std::cin >> months;
    
    std::cout << std::endl;
    switch (months)
    {
        case 1:
            std::cout << "El primer mes del año es Enero.";
            break;
        case 2:
            std::cout << "El segundo mes del año es Febrero.";
            break;
        case 3:
            std::cout << "El tercer mes del año es Marzo.";
            break;
        case 4:
            std::cout << "El cuarto mes del año es Abril.";
            break;
        case 5:
            std::cout << "El quinto mes del año es Mayo.";
            break;
        case 6:
            std::cout << "El sexto mes del año es Junio.";
            break;
        case 7:
            std::cout << "El septimo mes del año es Julio.";
            break;
        case 8:
            std::cout << "El octavo mes del año es Agosto.";
            break;
        case 9:
            std::cout << "El noveno mes del año es Septiembre.";
            break;
        case 10:
            std::cout << "El decimo mes del año es Octubre.";
            break;
        case 11:
            std::cout << "El undecimo mes del año es Noviembre.";
            break;
        case 12:
            std::cout << "El decimosegundo mes del año es Diciembre.";
            break;
        default:
            std::cout << "No esta en e rango valido\n";
            break;
    }
    std::cout << std::endl;

    return 0;
}