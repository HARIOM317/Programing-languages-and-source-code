#include<iostream>

using namespace std;

int main()
{
    int n;
    cout<<"Enter value of row and column for a square matrix[NxN] : "<<endl;
    cin>>n;
    cout<<"Enter elements of square matrix:"<<endl;
    int arr[n][n];
    for (int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++){
            cin>>arr[i][j];
        }
    }
    for (int i = 0; i < n; i++)
    {
        for(int j = i; j < n; j++){
            int temp = arr[i][j];
            arr[i][j] = arr[j][i];
            arr[j][i] = temp;
        }
    }
    cout<<"\n\nTranspose matrix is: \n\n";
    for (int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++){
            cout<<arr[i][j]<<" ";
        }cout<<"\n";
    }
    
    cout<<"\n\n";
    return 0;
}