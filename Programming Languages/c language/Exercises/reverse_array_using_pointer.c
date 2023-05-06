#include <stdio.h>

int reverse_array(int *arr, int n)
{
    int temp;
    for (int i = 0; i < (n / 2); i++)
    {
        temp = arr[i];
        arr[i] = arr[n - i - 1];
        arr[n - i - 1] = temp;
    }
}

int main()
{
    int arr[] = {18, 22, 31, 14, 57, 60, 77, 82, 94, 10};

    reverse_array(arr, 10);

    printf("Reverse array is: \n");
    for (int i = 0; i < 10; i++)
    {
        printf("%d ", arr[i]);
    }

    return 0;
}