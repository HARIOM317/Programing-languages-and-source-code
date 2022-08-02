#include<stdio.h>

int main(){
    int i=0, n, sum=0;
    printf("***ENTER THE NUMBER AS FAR YOU WANT TO SUM*** \n");
    scanf("%d", &n);
    do{
        sum+=i;
        i++;
    }while(i<=n);
    printf("SUM OF FIRST %d NATURAL NUMBER IS %d \n", n, sum);
    return 0;
}