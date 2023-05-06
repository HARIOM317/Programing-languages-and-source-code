#include <stdio.h>

// Using recursive function
double factorial_of_n_recursion(int num)
{
    if (num == 0)
    {
        return 1;
    }
    else if (num == 1)
    {
        return 1;
    }
    return factorial_of_n_recursion(num - 1) * num;
}

// Using non-recursive function
double factorial_of_n(int num)
{
    double fact = 1;
    for (int i = num; i > 0; i--)
    {
        fact = fact * i;
    }
    return fact;
}

int main()
{
    int number;
    printf("Enter number : ");
    scanf("%d", &number);

    printf("Factorial of %d using non-recursive function is : %f \n", number, factorial_of_n(number));
    printf("Factorial of %d using recursive function is : %f \n", number, factorial_of_n_recursion(number));

    return 0;
}