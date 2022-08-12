#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int n;
    cout << "Enter a number: ";
    cin >> n;
    bool flag = 0;
    for (int i = 2; i <= sqrt(n); i++)
    {
        if (n % i == 0)
        {
            cout << "Not a prime number " << endl;
            flag = 1;
            break;
        }
    }

    if (flag == 0)
    {
        cout << "Prime Number" << endl;
    }

    return 0;
}