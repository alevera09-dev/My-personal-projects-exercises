/*4. Hacer una matriz preguntando al usuario el numero de filas y columnas,
llenarlo de numeros aleatorios, copiar el contenido a otra matriz
y por ultimo mostrarla en pantalla. */

#include <iostream>
#include <ctime>
#include <cstdlib>

int main(void)
{
    using std::cout, std::cin, std::endl;
    srand(time(NULL));

    int fila, col;

    do
    {
        cout << "Digita el valor de filas que tendra la matriz: ";
        cin >> fila;
    } while(fila <= 0);

    do
    {
        cout << "Digita el valor de columnas que tendra la matriz: ";
        cin >> col;
    } while(col <= 0);

    int matriz[fila][col];

    for (int i = 0; i < fila; i++)
    {
        for (int j = 0; j < col; j++)
        {
            matriz[i][j] = 1 + rand() % 100;
        }
    }

    for (int i = 0; i < fila; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cout << matriz[i][j] << ' ';
        }
        cout << endl;
    }

    return 0;
}