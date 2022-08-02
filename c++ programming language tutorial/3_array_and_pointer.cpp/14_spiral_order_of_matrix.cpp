#include<iostream>

using namespace std;

int main()
{
    int m, n;
    cout<<"Enter number of rows: ";
    cin>>m;
    cout<<"Enter number of columns: ";
    cin>>n;
    cout<<"Enter elements: "<<endl;
    int arr[m][n];
    for (int i = 0; i < m; i++)
    {
        for(int j = 0; j < n; j++){
            cin>>arr[i][j];
        }
    }
    cout<<"\n\nSPIRAL ORDER IS:\n\n";
    int row_start=0,row_end=m-1,column_start=0,column_end=n-1;
    while (row_start<=row_end && column_start<=column_end){
        
        //FOR ROW START

        for(int column= column_start; column<=column_end; column++){
            cout<<arr[row_start][column]<<" ";
        }
        row_start++;

        //FOR COLUMN END

        for(int row=row_start; row<=row_end; row++){
            cout<<arr[row][column_end]<<" ";
        }
        column_end--;

        //FOR ROW END

        for(int column=column_end; column>=column_start; column--){
            cout<<arr[row_end][column]<<" ";
        }
        row_end--;

        //FOR COLUMN START

        for(int row=row_end; row>=row_start; row--){
            cout<<arr[row][column_start]<<" ";
        }
        column_start++;
    }
    cout<<"\n\n";
    return 0;
}