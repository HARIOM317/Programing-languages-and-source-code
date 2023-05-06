#include <stdio.h>

int isPrime(int number)
{
    for (int i = 2; i < number; i++)
    {
        if (number % i == 0)
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    int number;
    printf("\nEnter number : ");
    scanf("%d", &number);
    printf("\nPrime numbers between 2 to %d are as follow:\n", number);

    int flag = 1;
    for (int i = 2; i < number; i++)
    {
        if (number % i == 0)
        {
            flag = 0;
        }

        if (isPrime(i))
        {
            printf("%d ", i);
        }
    }

    if (flag == 1)
    {
        printf("\n\nGiven number is a prime number\n\n");
    }
    else
    {
        printf("\n\nGiven number is not a prime number\n\n");
    }

    return 0;
}