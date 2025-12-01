/* Esercizio trentacinque

    Suma de los primeros 10 numeros pares
    
*/

#include <stdio.h>

int main(void)
{
    int suma = 0;
    for (int i = 2; i <= 20; i += 2)
    {
        suma += i;
        printf("%i\n", suma);
    }
    

    return 0;
}