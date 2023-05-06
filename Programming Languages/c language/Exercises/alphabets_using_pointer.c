#include <stdio.h>

char print_alphabets(char *arr)
{
    char c;
    for (int i = 0, c = 'a'; i < 26, c <= 'z'; i++, c++)
    {
        arr[i] = c;
    }
}

int main()
{
    char arr[26] = {};
    print_alphabets(arr);

    for (int i = 0; i < 26; i++)
    {
        printf("%c ", arr[i]);
    }

    return 0;
}