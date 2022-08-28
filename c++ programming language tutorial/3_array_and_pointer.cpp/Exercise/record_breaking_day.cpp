#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cout << "Enter size of array : ";
    cin >> n;
    int arr[n + 1];
    arr[n] = -1;

    cout << "enter array elements : \n";

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    if (n == 1)
    {
        cout << "1" << endl;
        return 0;
    }

    int ans = 0;
    int maximum = -1;

    for (int i = 0; i < n; i++)
    {
        if (arr[i] > maximum && arr[i] > arr[i + 1])
        {
            ans++;
        }
        maximum = max(maximum, arr[i]);
    }

    cout << "Number of record breaking days are : " << ans << endl;

    return 0;
}