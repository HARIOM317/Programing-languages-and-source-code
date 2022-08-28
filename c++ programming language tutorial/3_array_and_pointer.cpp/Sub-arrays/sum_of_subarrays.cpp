#include <iostream>

using namespace std;

int main()
{
    int n;
    cout << "Enter the value of n" << endl;
    cin >> n;
    int arr[n];
    cout << "Enter array elements :\n";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << "\n\n";
    int current = 0;
    for (int i = 0; i < n; i++)
    {
        current = 0;
        for (int j = i; j < n; j++)
        {
            current += arr[j];
            cout << current << endl;
        }
    }

    cout << "\n\n";

    return 0;
}