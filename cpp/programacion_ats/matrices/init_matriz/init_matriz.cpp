/*1. Hacer un programa para rellenar ina matriz pidiendo al usuario el numero de filas
y columnas, Posteriormente mostrer la matriz en pantalla.*/

#include<iostream>

int main(void)
{
    using std::cout, std::cin, std::endl;

    int col, line;

    do
    {
        cout << "Digita el valor de filas que tendra la matriz: ";
        cin >> line;
    } while(line <= 0);

    do
    {
        cout << "Digita el valor de columnas que tendra la matriz: ";
        cin >> col;
    } while(col <= 0);


    int matriz[line][col];

    for (int i = 0; i < line; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cout << "Digita el valor de la posicion(" << i << "," << j << ") de la matriz: ";
            cin >> matriz[i][j];
        }
    }

    for (int i = 0; i < line; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cout << '(' << i << ',' << j << ") " << matriz[i][j] << endl;
        }
    }

    return 0;

}