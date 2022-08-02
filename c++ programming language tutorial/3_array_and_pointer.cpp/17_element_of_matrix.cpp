#include <iostream>

using namespace std;

int main()
{
    int n, m;
    cout << "Enter size of rows: ";
    cin >> n;
    cout << "Enter size of columns: ";
    cin >> m;
    cout << "Enter matrix elements: " << endl;
    int arr[n][m];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> arr[i][j];
        }
    }
    int target;
    cout << "Which element youu want to found" << endl;
    cin >> target;
    int r = 0, c = m - 1;
    bool found = false;
    while (r < n and c >= 0)
    {
        if (arr[r][c] == target)
        {
            found = true;
        }
        if (arr[r][c] > target)
        {
            c--;
        }
        else
        {
            r++;
        }
    }

    if (found)
    {
        cout << "Element found in matrix";
    }
    else
    {
        cout << "Element does not exist in matrix";
    }
    return 0;
}