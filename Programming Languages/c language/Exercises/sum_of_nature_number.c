#include<stdio.h>

int main(){
    int i=1, n, sum=0;
    printf("***ENTER A NATURAL NUMBER AS FAR AS YOU WANT TO SUM*** \n ");
    scanf("%d", &n);
    while(i<=n){
        sum+=i;
        i++;
    } 
    printf("the sum of first %d natural number is %d \n", n, sum);
    return 0;
}