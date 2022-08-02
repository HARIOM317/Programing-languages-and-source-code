#include<stdio.h>

int main(){
    int a;
    printf("Enter a\n");
    scanf("%d", &a);

    (a<25) ? printf("a is less then 25") : printf("a is greater then 25");
    return 0;
}