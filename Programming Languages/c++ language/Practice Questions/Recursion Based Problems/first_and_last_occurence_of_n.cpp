#include <iostream>

using namespace std;

int first_occurrence(int arr[], int n, int i, int key)
{
    if (i == n)
    {
        return -1;
    }
    if (arr[i] == key)
    {
        return i;
    }
    return first_occurrence(arr, n, i + 1, key);
}

int last_occurrence(int arr[], int n, int i, int key)
{
    if (i == n)
    {
        return -1;
    }

    int restArray = last_occurrence(arr, n, i + 1, key);
    if (restArray != -1)
    {
        return restArray;
    }
    if (arr[i] == key)
    {
        return i;
    }
    return -1;
}

int main()
{
    int arr[10] = {2, 4, 5, 2, 0, 1, 8, 4, 9, 4};
    cout << "First occurrence : " << first_occurrence(arr, 10, 0, 2) << endl;
    cout << "Last occurrence : " << last_occurrence(arr, 10, 0, 2) << endl;

    return 0;
}