#include<iostream>
#include<functional>
#include<algorithm>

using namespace std;

int main()
{
    int arr[] = {4,7,57,1,2,87,65,41,21,74,3,12,11,4,6};
    sort(arr, arr+15);
    cout<<"Sorting in accending order: "<<endl;
    for (int i = 0; i < 15; i++)
    {
        cout<<arr[i]<<" ";
    }cout<<"\n\n";

    cout<<"Sorting in deccending order: "<<endl;
    sort(arr, arr+15, greater<int>());
    for (int i = 0; i < 15; i++)
    {
        cout<<arr[i]<<" ";
    }cout<<"\n\n";

    return 0;
}