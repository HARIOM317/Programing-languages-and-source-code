#include<stdio.h>

int main(){
    int x,y,z;
    printf("Enter first number =\n");
    scanf("%d", &x);
    printf("Enter Second number =\n");
    scanf("%d", &y);
    printf("the sum of these numbers = %d\n", x+y);
    printf("the substraction of these numbers = %d\n", x-y);
    printf("the product of these numbers = %d\n", x*y);
    printf("the devision of these numbers = %d\n", x/y);
    printf("the remainder of these numbers = %d\n", x%y);

    return 0;
}