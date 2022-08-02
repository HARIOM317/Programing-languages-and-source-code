#include <iostream>
using namespace std;

int main()
{
    int row, column, i, j, flag1 = 0, flag2 = 0;

    cout << "Enter rows and columns of matrix: ";
    cin >> row >> column;
    if (row != column)
    {
        cout << "This is not a square matrix..";
        exit(0);
    }
    else
    {
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

        for (int i = 0; i < row; i++)
        {
            for (int j = 0; j < column; j++)
            {
                if (mat[i][j] != trans_mat[i][j])
                {
                    flag1 = 1;
                    break;
                }
                else if (mat[i][j] == -trans_mat[i][j])
                {
                    flag2 = 1;
                    break;
                }
            }
        }
        if (flag1 == 0)
        {
            cout << "\nThis is a symmetric matrix!" << endl;
        }
        else if (flag2 == 1)
        {
            cout << "\nThis is a skew symmetric matrix!" << endl;
        }
        else
        {
            cout << "\nIt is neither symmetric nor skew-symmetric.\n ";
        }
    }

    return 0;
}