#include <iostream>

using namespace std;

bool sorting(int arr[], int n)
{
    if (n == 1)
    {
        return true;
    }
    bool restArray = sorting(arr + 1, n - 1);
    if ((arr[0] < arr[1] && restArray == true))
    {
        return true;
    }
}

int main()
{
    int n;
    cout << "Enter size of array : ";
    cin >> n;
    int arr[n];
    cout << "Enter array elements:\n";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int ans = sorting(arr, n);
    if (ans == 1)
    {
        cout << "Given array is sorted!";
    }
    else
    {
        cout << "Given array is not sorted!";
    }

    return 0;
}