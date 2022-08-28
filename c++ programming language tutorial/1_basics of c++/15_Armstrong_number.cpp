#include <iostream>

using namespace std;

int main()
{
    int n;
    cout << "Enter a number" << endl;
    cin >> n;
    int sum = 0;
    int original_number = n;
    while (n > 0)
    {
        int last_digit = n % 10;
        sum += (last_digit * last_digit * last_digit);
        n = n / 10;
    }
    if (sum == original_number)
    {
        cout << "ARMSTRONG NUMBER" << endl;
    }
    else
    {
        cout << "NOT A ARMSTRONG NUMBER" << endl;
    }

    return 0;
}