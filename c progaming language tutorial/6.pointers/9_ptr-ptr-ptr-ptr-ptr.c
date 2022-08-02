#include<stdio.h>

int main(){
    int i;
    printf("Enter a number \n");
    scanf("%d", &i);
    int*a= &i;
    int**b= &a;
    int***c= &b;
    int****d= &c;
    int*****e= &d;
    printf("the value of i is %d \n", *****e);
    return 0;
}