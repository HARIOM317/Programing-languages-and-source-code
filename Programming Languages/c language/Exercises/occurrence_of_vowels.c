#include <stdio.h>
#include <string.h>

int occurrence_of_vowels(char str[])
{
    int count_vowels = 0;
    for (int i = 0; str[i] != '\0'; i++)
    {
        if (str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u')
        {
            count_vowels++;
        }
    }
    return count_vowels;
}

int main()
{
    char str[100];
    printf("Enter a string : ");
    gets(str);

    printf("Vowels = %d\n", occurrence_of_vowels(str));

    return 0;
}