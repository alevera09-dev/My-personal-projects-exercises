/*3. Hacer una matriz de tipo entero de 2*2, llenala de numeros y luego copiar todo
su contenido contenido hacia otra matriz. */

#include <iostream>

int main(void)
{
    using std::cout, std::endl;

    int arr_2d[2][2] = {{1, 2}, {3, 4}};
    int cp_arr_2d[2][2];

    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            cp_arr_2d[i][j] = arr_2d[i][j];
        }
    }

    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            cout << '[' << i << ']' << '[' << j << ']' << '(' << arr_2d[i][j] << ')' << endl;
            cout << '[' << i << ']' << '[' << j << ']' << '(' << cp_arr_2d[i][j] << ')' << endl;
        }
    }
    return 0;
}