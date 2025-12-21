/*5. Escriba un programa que lea de la entrada estandar un caracter e indique 
en la salida estandar si el caracter es una vocal minuscula o no
*/

#include <iostream>

int main(void)
{
    char vowel;
    std::cout << "Digita una vocal: ";
    std::cin >> vowel;
    
    switch (vowel)
    {
        case 'a':
            std::cout << "\nEs a minuscula\n";
            break;
        case 'e':
            std::cout << "\nEs e minuscula\n";
            break;
        case 'i':
            std::cout << "\nEs i minuscula\n";
            break;
        case 'o':
            std::cout << "\nEs o minuscula\n";
            break;
        case 'u':
            std::cout << "\nEs u minuscula\n";
            break;
        case 'A':
            std::cout << "\nEs A mayuscula\n";
            break;
        case 'E':
            std::cout << "\nEs E mayuscula\n";
            break;
        case 'I':
            std::cout << "\nEs I mayuscula\n";
            break;
        case 'O':
            std::cout << "\nEs O mayuscula\n";
            break;
        case 'U':
            std::cout << "\nEs U mayuscula\n";
            break;
        default:
            std::cout << "\nEs otro caracter\n";
            break;
    }
    
    return 0;
}