/*Hacer un array de 5 valores y luego que el programa los ponga en otro array con los mismos valores multiplicados por 2*/

#include <iostream>

int main(void)
{
    using std::cout, std::cin, std::endl;

    int arr[] = {1, 2, 3, 4, 5};
    
    int arra2[5];
    for (int i = 0; i < 5; i++)
    {
        arra2[i] = arr[i] * 2;
    }

    for (int i = 0; i < 5; i++)
    {
        cout << arr[i] << endl;
        cout << arra2[i] << endl;
    }
    return 0;
}