#include<iostream>
using namespace std;
int main ()
{
    int i, j, m, n, flag = 0;
    cout << "Enter number of rows and columns : ";
    cin >> m >> n;
    if (m != n)
    {
        cout << "Matrix is not a square matrix!";
        exit(0);
    }
    float A[m][n];
    cout << "Enter array elements : "<<endl;
    for (i = 0; i < m; i++)
        for (j = 0; j < n; j++)    
            cin >> A[i][j];
    for (i = 0; i < m; i++)
        for (j = 0; j < n; j++)
        {
            if ((A[i][j] != 1) && (A[j][i] != 0))
            {
                flag = 1;
                break;
            }
        }
    if (flag == 0)
        cout << "The given array is an identity matrix.\n ";
    else
        cout << "The given array is not an identity matrix.\n ";
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)	
            cout << A[i][j] << " ";
        cout << "\n ";
    }
    return 0;
}