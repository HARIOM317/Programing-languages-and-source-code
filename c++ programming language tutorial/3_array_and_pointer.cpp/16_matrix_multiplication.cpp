#include<iostream>

using namespace std;

int main()
{
    int n1, n2, n3;
    cin>> n1 >> n2 >> n3;
    int matrix_1[n1][n2];
    int matrix_2[n2][n3];
    for (int i = 0; i < n1; i++)
    {
        for(int j = 0; j < n2; j++){
            cin>>matrix_1[i][j];
        }
    }
    for (int i = 0; i < n2; i++)
    {
        for(int j = 0; j < n3; j++){
            cin>>matrix_2[i][j];
        }
    }
    int ans[n1][n3];
     for (int i = 0; i < n1; i++)
    {
        for(int j = 0; j < n3; j++){
            ans[i][j] = 0;
        }
    }
     for (int i = 0; i < n1; i++)
    {
        for(int j = 0; j < n3; j++){
            for(int k = 0; k < n2; k++){
                ans[i][j] += matrix_1[i][k]*matrix_2[k][j];
            }
        }
    }
    for (int i = 0; i < n1; i++)
    {
        for(int j = 0; j < n3; j++){
            cout<<ans[i][j]<<" ";
        }cout<<endl;
    }
    
    
    return 0;
}