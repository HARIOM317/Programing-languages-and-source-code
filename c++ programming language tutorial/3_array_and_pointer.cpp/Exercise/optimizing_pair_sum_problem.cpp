#include <bits/stdc++.h>

using namespace std;

bool pairSum(int arr[], int n, int k)
{
    int low = 0;
    int high = n - 1;

    while (low < high)
    {
        if (arr[low] + arr[high] == k)
        {
            cout << low << " " << high << endl;
            return true;
        }
        else if (arr[low] + arr[high] > k)
        {
            high--;
        }
        else
        {
            low++;
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