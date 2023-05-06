// C++ program to print Identity Matrix
#include<bits/stdc++.h>
using namespace std;
 
int Identity(int num)
{
    int row, col;
     
    for (row = 0; row < num; row++)
    {
        for (col = 0; col < num; col++)
        {
            // Checking if row is equal to column
            if (row == col)
                cout << 1 << " ";
            else
                cout << 0 << " ";
        }
        cout << endl;
    }
    return 0;
}
 
int main()
{
    int size;
    cout<<"Enter size of identity matrix: ";

    cin>>size;
    Identity(size);
    return 0;
}