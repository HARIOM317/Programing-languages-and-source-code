#include <iostream>

using namespace std;

int main()
{
    int row, column;
    cout << "Enter order of matrix:";
    cin >> row >> column;

    int mat[row][column], i, j;
    float determinant = 0;

    cout << "Enter elements of matrix row wise:\n";
    for (i = 0; i < row; i++)
        for (j = 0; j < column; j++)
            cin >> mat[i][j];

    printf("\nGiven matrix is:");
    for (i = 0; i < row; i++)
    {
        cout << "\n";

        for (j = 0; j < column; j++)
            cout << mat[i][j] << "\t";
    }

    // finding determinant
    for (i = 0; i < 3; i++)
        determinant = determinant + (mat[0][i] * (mat[1][(i + 1) % 3] * mat[2][(i + 2) % 3] - mat[1][(i + 2) % 3] * mat[2][(i + 1) % 3]));

    cout << "\n\ndeterminant: " << determinant;

    if (determinant == 0)
    {
        cout << "\nInverse is not possible of given matrix because determinant is 0 " << endl;
    }
    else
    {

        cout << "\n\nInverse of matrix is: \n";
        for (i = 0; i < row; i++)
        {
            for (j = 0; j < column; j++)
                cout << ((mat[(j + 1) % 3][(i + 1) % 3] * mat[(j + 2) % 3][(i + 2) % 3]) - (mat[(j + 1) % 3][(i + 2) % 3] * mat[(j + 2) % 3][(i + 1) % 3])) / determinant << "\t";

            cout << "\n";
        }
    }

    return 0;
}