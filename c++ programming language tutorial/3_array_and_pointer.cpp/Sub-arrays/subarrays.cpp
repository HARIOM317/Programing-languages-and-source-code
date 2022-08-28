#include <iostream>

using namespace std;

int main()
{
    int n;
    cout << "Enter size of array : ";
    cin >> n;
    cout << "Enter array elements : \n";
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << "all possible sub arrays are: \n\n";

    for (int i = 0; i < n; i++)
    {
        for (int j = i; j < n; j++)
        {
            for (int k = i; k <= j; k++)
            {
                cout << arr[k] << " ";
            }
            cout << endl;
        }
    }

    cout << "\n\n";
    return 0;
}