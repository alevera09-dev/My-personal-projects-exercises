/*4. Escriba un programa que tome cada 4 horas la temperatura exterior,
leyendola durante un periodo de 24 horas. Es decir debe leer 6 temperaturas.
Calcule la temperatura media del dia, la temperatura mas alta y la mas baja
*/

#include <iostream>

int main(void)
{
    int hours, temp, max_temp, min_temp, sum = 0;

    do
    {
        std::cout << "Digita la cantidad de bloques de 4 horas que registraras la temperatura: ";
        std::cin >> hours;
    } while (hours < 1);

    std::cout << std::endl;
    for (int i = 0; i < hours; i++)
    {
        std::cout << "Digita una temperatura: ";
        std::cin >> temp;

        if (i == 0)
        {
            max_temp = temp;
            min_temp = temp;
        }
        else if (temp > max_temp)
        {
            max_temp = temp;
        }
        else if (temp < min_temp)
        {
            min_temp = temp;
        }

        sum += temp;
    }
    
    std::cout << "\nLa temperatuda media del dia: " << sum / hours;
    std::cout << "\nLa temperatura minima del dia: " << min_temp;
    std::cout << "\nLa temperatura maxima del dia: " << max_temp << std::endl;

    return 0;
}