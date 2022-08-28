#include <iostream>

using namespace std;

void decreasing(int n)
{
    if (n == 0)
    {
        return;
    }
    cout << n << " ";
    decreasing(n - 1);
}

void increasing(int n)
{
    if (n == 0)
    {
        return;
    }
    increasing(n - 1);
    cout << n << " ";
}

int main()
{
    int n;
    cout << "Enter a number: ";
    cin >> n;
    cout << "Decreasing order: \n";
    decreasing(n);
    cout << "\nIncreasing order: \n";
    increasing(n);

    return 0;
}