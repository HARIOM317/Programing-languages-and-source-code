#include <iostream>

using namespace std;

int factorial(int n)
{
    int fact = 1;

    for (int i = 1; i <= n; i++)
    {
        fact *= i;
    }
    return fact;
}

int main()
{
    int n, r;
    cout << "Enter value of n : ";
    cin >> n;
    cout << "Enter value of r : ";
    cin >> r;

    int nCr = factorial(n) / ((factorial(n - r)) * factorial(r));
    cout << "nCr = " << nCr;
    return 0;
}