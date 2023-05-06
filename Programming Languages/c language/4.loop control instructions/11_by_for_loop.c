#include<stdio.h>

int main(){
    int i, n, sum=0;
    printf("***ENTER THE NUMBER AS FAR YOU WANT TO SUM*** \n");
    scanf("%d", &n);
    for(i=1; i<=n; i++){
        sum+=i;
    }
        printf("THE SUM OF FIRST %d NATURAL NUMBER IS %d \n", n, sum);
    return 0;
}