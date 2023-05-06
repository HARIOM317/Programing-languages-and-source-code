#include<stdio.h>

int main(){
    int n, factorial=1;
    printf("enter a number for factorial\n");
    scanf("%d", &n);
    for( int i=1; i<=n; i++){
        factorial*=i;
    }
    printf("the factorial of given number is %d\n", factorial);
    return 0;
}