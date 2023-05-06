#include <bits/stdc++.h>

using namespace std;

int a[10][10], i, j, m, n;

int rank_matrix(int, int);
void swap(int, int, int);
void read(int, int);
void display(int, int);

int main()
{
    int rnk;
    cout << "Enter order of matrix (Rows and Columns size): ";
    cin >> m >> n;
    read(m, n);
    display(m, n);
    rnk = rank_matrix(m, n);
    cout << "\n\nThe rank of above matrix is: \n\n"
         << rnk;
    return 0;
}

void read(int r, int c)
{
    cout << "Enter " << r << "x" << c << " order matrix value (Row by rows): \n";
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            cin >> a[i][j];
        }
    }
}

void display(int r, int c)
{
    cout << "Matrix is: " << endl;
    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            cout << a[i][j] << "  ";
        }
        cout << endl;
    }
}

void swap(int r1, int r2, int c)
{
    int t;
    for (i = 0; i < c; i++)
    {
        t = a[r1][i];
        a[r1][i] = a[r2][i];
        a[r2][i] = t;
    }
}

int rank_matrix(int r1, int c1)
{
    int i, j, k;
    float ratio;
    for (i = 0; i < c1; i++)
    {
        cout << "\nstep = " << i + 1 << endl;
        display(m, n);
        if (a[i][i] != 0)
            for (j = 0; j < r1; j++)
                if (j != i)
                {
                    ratio = a[j][i] / a[i][i];
                    for (k = 0; k < c1; k++)
                        a[j][k] -= ratio * a[i][k];
                }
                else
                    cout << endl;
        else
        {
            for (j = i + 1; j < r1; j++)
                if (a[j][i] != 0)
                {
                    swap(i, j, c1);
                    break;
                }
            if (j == r1)
            {
                c1--;
                for (j = 0; j < r1; j++)
                {
                    a[j][i] = a[j][c1];
                }
            }
            i--;
        }
    }
    return c1;
}