#include <iostream>

using namespace std;

int main()
{
    int n;
    cout << "Enter a number" << endl;
    cin >> n;

    // Using first logic
    cout << "Pattern using logic 1: \n";
    for (int i = 1; i <= n; i++)
    {
        int j;
        for (j = 1; j <= n - i; j++)
        {
            cout << "  ";
        }
        for (int j = 1; j <= 2 * i - 1; j++)
        {
            cout << "*"
                 << " ";
        }
        cout << endl;
    }

    for (int i = 1; i <= n; i++)
    {
        int j;
        for (j = 1; j < i; j++)
        {
            cout << "  ";
        }
        for (int j = 1; j <= (2 * n) - (2 * i) + 1; j++)
        {
            cout << "*"
                 << " ";
        }
        cout << endl;
    }

    // Using second logic
    cout << "Pattern using logic 2: \n";
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n - i; j++)
        {
            cout << "  ";
        }
        for (int j = 1; j <= 2 * i - 1; j++)
        {
            cout << "* ";
        }
        cout << endl;
    }

    for (int i = n; i >= 1; i--)
    {
        for (int j = 1; j <= n - i; j++)
        {
            cout << "  ";
        }
        for (int j = 1; j <= 2 * i - 1; j++)
        {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}