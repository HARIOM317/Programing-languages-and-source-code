#include <iostream>

using namespace std;

int main()
{
    int a, b;
    cout << "Enter starting number" << endl;
    cin >> a;
    cout << "Enter ending number" << endl;
    cin >> b;
    for (int num = a; num <= b; num++)
    {
        int i;
        for (i = 2; i < num; i++)
        {
            if (num % i == 0)
            {
                break;
            }
        }
        if (i == num)
        {
            cout << num << "\t";
        }
    }

    return 0;
}