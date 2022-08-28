#include <bits/stdc++.h>

using namespace std;

int main()
{
    // PROGRAM FOR MAXIMUM SUM OF SUB ARRAY OF GIVEN ARRAY
    int n;
    cout << "Enter size of array : " << endl;
    cin >> n;
    int arr[n];
    cout << "Enter array elements : \n";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << "\n\n";

    int currSum[n + 1];
    currSum[0] = 0;

    for (int i = 1; i <= n; i++)
    {
        currSum[i] = currSum[i - 1] + arr[i - 1];
    }

    int maxSum = INT_MIN;
    for (int i = 1; i <= n; i++)
    {
        int sum = 0;
        for (int j = 0; j < i; j++)
        {
            sum = currSum[i] - currSum[j];
            maxSum = max(sum, maxSum);
        }
    }

    cout << "Maximum sum of sub array is: " << maxSum << endl;
    cout << "\n\n";
    return 0;
}