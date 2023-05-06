#include <stdio.h>
#include <string.h>

void slicing(char str[], int m, int n);

int main()
{
    char str[100];
    printf("Enter a string : ");
    gets(str);
    int starting_index, ending_index;
    printf("Enter starting index of string : ");
    scanf("%d", &starting_index);
    printf("Enter ending index of string : ");
    scanf("%d", &ending_index);

    slicing(str, starting_index, ending_index);

    return 0;
}

void slicing(char str[], int m, int n)
{
    for (int i = m; i <= n; i++)
    {
        printf("%c", str[i]);
    }
}
