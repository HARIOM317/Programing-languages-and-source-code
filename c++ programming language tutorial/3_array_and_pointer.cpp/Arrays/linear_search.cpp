#include<iostream>

using namespace std;

int linearSearch(int arr[], int n, int key){
    for (int i = 1; i <= n; i++)
    {
        if (arr[i]==key)
        {
            cout<<"this element is present on number: ";
            return i;
        }
        
    }
    
    return -1;
}

int main()
{
    int n;
    cout<<"Enter the number of elements "<<endl;
    cin>>n;
    int arr[n];
    for (int i = 1; i <= n; i++)
    {
        cin>>arr[i];
    }
    int key;
    cout<<"Enter key which you want to search"<<endl;
    cin>>key;

    cout<<linearSearch(arr, n, key)<<endl;
    
    return 0;
}