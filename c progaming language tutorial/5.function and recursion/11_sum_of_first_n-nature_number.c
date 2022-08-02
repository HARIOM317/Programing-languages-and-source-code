#include<stdio.h>
int sum(int);
int main(){
    int n;
    printf("Enter the number \n");
    scanf("%d",&n);
    printf("the sum of first %d nature number is %d \n", n, sum(n));
    return 0;
}
int sum(int n){
   int result = n*(n+1)/2;
    return result;
}