#include <iostream>

using namespace std;

int main()
{
    //PROGRAM FOR PRINT RECTANGLE STAR PATTERNS.

    int row, column;

    cout << "\n\n";

    cout << "How many rows you want to print" << endl;
    cin >> row;

    cout << "How many columns you want to print" << endl;
    cin >> column;

    cout << "\n\n";

    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < column; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
    cout << "\n\n";

    return 0;
}