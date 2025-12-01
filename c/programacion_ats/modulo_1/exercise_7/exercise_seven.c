/* Esercize sette

    Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto
    debera pagar finalmente por su compra.

*/

#include<stdio.h>

int main(void)
{
    float total_compra, pago_final, descuento = 0.15;

    printf("\nTotal de la compra: "); scanf("%f", &total_compra);

    pago_final = total_compra - (total_compra * descuento);

    printf("\nEl pago final con el descuento del 15 porciento es: %.2f\n", pago_final);

    return 0;
}