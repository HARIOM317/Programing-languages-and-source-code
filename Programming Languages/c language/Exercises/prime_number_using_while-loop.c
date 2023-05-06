#include<stdio.h>

int main(){
    int i=2,n;
    int prime=1;
    printf("enter a number \n");
    scanf("%d",&n);
    while(i<n){
        if(n%i==0){
            prime =0;
            break;
        }
        i++;
    }

        if(prime==0){
            printf("%d is not a prime number \n", n);
        }
        else{
            printf("%d is a prime number", n);
        }
    return 0;
}