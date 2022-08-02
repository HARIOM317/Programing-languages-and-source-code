#include <iostream>

using namespace std;

int main()
{
    //PROGRAM FOR MAXIMUM SUM OF SUBARRAY OF GIVEN ARRAY
    int n;
    cout << "How many elements will be present in your array" << endl;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << "\n\n";
    int maxsum = INT_MIN;
    for (int i = 0; i < n; i++)
    {
        for (int j = i; j < n; j++)
        {
            int sum=0;
            for (int k = i; k <= j; k++)
            {
                sum+=arr[k];
            }
            maxsum = max(maxsum, sum);
        }
    }
    cout<<"Maximum sum of subarray is: "<<maxsum<<endl;
    cout << "\n\n";
    return 0;
}