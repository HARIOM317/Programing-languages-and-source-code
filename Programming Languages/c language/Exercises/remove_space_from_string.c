#include <stdio.h>

void remove_spaces(char str[])
{
    for (int i = 0; str[i] != '\0'; i++)
    {
        // ASCII value of space is 32
        if (str[i] == 32)
        {
            continue;
        }
        else
        {
            printf("%c", str[i]);
        }
    }
}

int main()
{
    char str[] = "Good Morning, Everyone!";
    remove_spaces(str);
    return 0;
}