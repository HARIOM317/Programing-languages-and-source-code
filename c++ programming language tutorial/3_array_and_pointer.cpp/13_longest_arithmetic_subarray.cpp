#include<iostream>

using namespace std;

int main()
{
    int n;
    cout<<"How many elements you want to enter"<<endl;
    cin>>n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin>>arr[i];
    }
    int ans = 2;
    int pd = arr[1] - arr[0];
    int j = 2;
    int current = 2;
    while (j<n)
    {
        if(pd==arr[j]-arr[j-1]){
            current++;
        }
        else{
            pd = arr[j]-arr[j-1];
            current=2;
        }
        ans = max(ans, current);
        j++;
    }
    
    cout<<"maximum arithmetic subarray = "<<ans<<endl;

    return 0;
}