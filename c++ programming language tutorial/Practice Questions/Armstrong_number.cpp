#include <iostream>

using namespace std;

int main()
{
    int n;
    cout << "Enter a number: ";
    cin >> n;
    int num = 0;
    int original_n = n;
    while (n > 0)
    {
        int lastDigit = n % 10;
        num += (lastDigit * lastDigit * lastDigit);
        n = n / 10;
    }
    if (num == original_n)
    {
        cout << "Armstrong Number";
    }
    else
    {
        cout << "Not a Armstrong number";
    }
    return 0;
}