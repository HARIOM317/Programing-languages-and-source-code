#include <stdio.h>

int main()
{
    int a = 54;
    int *ptr;
    int c = 44;
    printf("The address of ptr is %d \n", ptr);
    if (ptr != NULL)
    {
        printf("The value of a is %d \n", *ptr);
    }
    else
    {
        printf("The pointer is a null pointer and cannot be dereferenced \n");
    }
    return 0;
}