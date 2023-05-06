#include <iostream>

using namespace std;

int setBit(int n, int pos)
{
    return ((n & (1 << pos)) != 0);
}

void unique(int arr[], int n)
{
    int xor_sum = 0;
    for (int i = 0; i < n; i++)
    {
        xor_sum = xor_sum ^ arr[i];
    }
    int temp_xor = xor_sum;
    int setbit = 0;
    int pos = 0;
    while (setbit != 1)
    {
        setbit = xor_sum & 1;
        pos++;
        xor_sum = xor_sum >> 1;
    }
    int new_xor;
    for (int i = 0; i < n; i++)
    {
        if (setBit(arr[i], pos - 1))
        {
            new_xor = new_xor ^ arr[i];
        }
    }

    cout << new_xor << endl;
    cout << (temp_xor ^ new_xor) << endl;
}

int main()
{
    int arr[] = {1, 2, 3, 3, 2, 1, 8, 5};
    unique(arr, 8);
    return 0;
}