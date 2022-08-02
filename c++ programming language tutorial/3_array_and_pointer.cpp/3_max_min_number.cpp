#include<iostream>
#include<climits>

using namespace std;

int main()
{
    int n;
    cout<<"Enter the size of array"<<endl;
    cin>>n;
    int array[n];
    for (int i = 0; i < n; i++)
    {
        cin>>array[i];
    }
    int maxNo = INT_MIN;
    int minNo = INT_MAX;

    //THIS IS FIRST WAY TO PRINT MAX AND MIN NUMBERS

    for (int i = 0; i < n; i++)
    {
        if(array[i]>maxNo){
            maxNo = array[i];
        }
        if(array[i]<minNo){
            minNo = array[i];
        }
    }

    //THIS IS SECOND WAY TO PRINT MAX AND MIN NUMBERS

    for (int i = 0; i < n; i++)
    {
        maxNo = max(maxNo, array[i]); //max is a default function for print maximum number
        minNo = min(minNo, array[i]); //min is also a default function for print minimum number
    }
    

    cout<<"Maximum number is: "<<maxNo<<endl;
    cout<<"Minimum number is: "<<minNo<<endl;
    
    return 0;
}