/* Esercize venti

    Ingresar por teclado el nombre, la edad y el sexo de cualquier persona e imprima,
    solo si la persona es de sexo masculino y mayor de edad, el nombre de la persona.

*/

#include<ctype.h>
#include<stdio.h>
#include<string.h>
#include<strings.h>

int main(void)
{
    char name[61], genero[11];
    int edad;
    
    printf("\nCual es tu nombre?: ");
    if (fgets(name, sizeof(name), stdin) != NULL)
    {
        name[strcspn(name, "\n")] = 0;
    }

    printf("\nCual es tu genero?: ");
    if (fgets(genero, sizeof(genero), stdin) != NULL)
    {
        genero[strcspn(genero, "\n")] = 0;
    }

    printf("\nCual es tu edad?: "); scanf("%i", &edad);


    if (edad >= 18 && strcasecmp(genero, "masculino") == 0)
    {
        printf("\nEste es tu nombre: %s\n", name);
    }

    return 0;
}