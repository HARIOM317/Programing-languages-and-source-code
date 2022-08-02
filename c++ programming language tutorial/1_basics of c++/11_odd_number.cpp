#include <iostream>

using namespace std;

int main()
{
    int n;
    cout << "Enter the value of n " << endl;
    cin >> n;
    for (int i = 0; i <= n; i++)
    {
        if (i % 2 == 0)
        {
            continue;
        }
        else
        {
            cout <<i;
            cout<<"\t";
        }
    }

    return 0;
}