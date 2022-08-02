#include<iostream>

using namespace std;

int binarySearch(int arr[], int n, int key){
    int startingPoint = 0;
    int endingPoint = n;
    while (startingPoint<=endingPoint)
    {
        int midElement = (startingPoint+endingPoint)/2;
        if(arr[midElement]==key){
            cout<<"This element is present on number : ";
            return midElement;
        }
        else if(arr[midElement]>key){
            endingPoint = midElement-1;
        }
        else{
            startingPoint = midElement+1;
        }
    }

    return -1;
    
}

int main()
{
    int n;
    cout<<"Enter number of elements you want to enter"<<endl;
    cin>>n;
    int arr[n];
    for (int i = 1; i <= n; i++)
    {
        cin>>arr[i];
    }
    int key;
    cout<<"Enter key which index number you want to search"<<endl;
    cin>>key;
    
    cout<<binarySearch(arr, n, key)<<endl;

    return 0;
}