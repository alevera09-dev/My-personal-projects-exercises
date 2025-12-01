/* Esercize ventidue

    Una distribuidora de motocicletas tiene una promocion de fin del año
    que consiste en lo siguiente.
    Las motos marca Honda tienen un descuento del 5%, las marcas Yamaha del 8%
    y las Suzuki del 10%, las otras marcas 2%

*/

#include<stdio.h>
#include<string.h>
#include<strings.h>

int main(void)
{
    char marca[41];

    printf("\nCual es la marca comprada?: ");
    if (fgets(marca, sizeof(marca), stdin) != NULL)
    {
        marca[strcspn(marca, "\n")] = 0;
    }

    
    if (strcasecmp(marca, "honda") == 0)
    {
        printf("\nLa cantidad de el descuento es 5 porciento\n");
    }
    else if (strcasecmp(marca, "yamaha") == 0)
    {
        printf("\nLa cantidad de el descuento es 8 porciento\n");
    }
    else if (strcasecmp(marca, "suzuki") == 0)
    {
        printf("\nLa cantidad de el descuento es 10 porciento\n");
    }
    else
    {
        printf("\nLa cantidad de el descuento es 2 porciento\n");
    }


    return 0;
}