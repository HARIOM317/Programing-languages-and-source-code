#include <bits/stdc++.h>

using namespace std;

bool pairSum(int arr[], int n, int k)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (arr[i] + arr[j] == k)
            {
                cout << i << " " << j << endl;
                return true;
            }
        }
    }
    return false;
}

int main()
{
    int n;
    cout << "Enter size of array : ";
    cin >> n;
    int arr[n];

    cout << "Enter elements of array :\n";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int targetSum;
    cout << "Enter target sum : ";
    cin >> targetSum;

    cout << "Target sum = " << pairSum(arr, n, targetSum);

    return 0;
}