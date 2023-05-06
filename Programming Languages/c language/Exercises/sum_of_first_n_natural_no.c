#include <stdio.h>

// Using recursive function
int n_natural_no(int number)
{
    if (number == 1)
    {
        return 1;
    }
    return n_natural_no(number - 1) + number;
}

// Using non-recursive function
int nNaturalNumber(int number)
{
    int sum = 0;
    for (int i = number; i > 0; i--)
    {
        sum += i;
    }
    return sum;
}

int main()
{
    int number;
    printf("Enter number : ");
    scanf("%d", &number);
    printf("\nSum of first %d natural number using non-recursive function is : %d", number, nNaturalNumber(number));

    printf("\nSum of first %d natural number using recursive function is : %d", number, n_natural_no(number));

    return 0;
}