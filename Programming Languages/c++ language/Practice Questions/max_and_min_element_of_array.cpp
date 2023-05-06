#include <iostream>

using namespace std;

int main()
{
    int n;
    cout << "Enter size of array : ";
    cin >> n;

    int arr[n];

    cout << "Enter elements of array\n\n";

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int min = INT8_MAX;
    int max = INT8_MIN;

    for (int i = 0; i < n; i++)
    {
        if (arr[i] > max)
        {
            max = arr[i];
        }
        if (arr[i] < min)
        {
            min = arr[i];
        }
    }

    cout << "Maximum element is : " << max << endl;
    cout << "Minimum element is : " << min << endl;

    return 0;
}