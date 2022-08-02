#include <iostream>
using namespace std;

int main()
{
    int row, column, i, j;

    cout << "Enter rows and columns of matrix: ";
    cin >> row >> column;

    int mat[row][column], trans_mat[column][row];

    cout << "\nEnter elements of matrix: " << endl;

    for (int i = 0; i < row; ++i)
    {
        for (int j = 0; j < column; ++j)
        {
            cin >> mat[i][j];
        }
    }

    cout << "\nEntered Matrix: " << endl;
    for (int i = 0; i < row; ++i)
    {
        for (int j = 0; j < column; ++j)
        {
            cout << " " << mat[i][j];
        }
        cout << endl;
    }

    for (int i = 0; i < row; ++i)
        for (int j = 0; j < column; ++j)
        {
            trans_mat[j][i] = mat[i][j];
        }

    cout << "\nTranspose of Matrix: " << endl;
    for (int i = 0; i < column; ++i)
    {
        for (int j = 0; j < row; ++j)
        {
            cout << " " << trans_mat[i][j];
        }
        cout << endl;
    }

    return 0;
}