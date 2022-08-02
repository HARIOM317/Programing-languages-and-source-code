#include<stdio.h>

int main(){
    int i, n;
    int prime=1;
    printf("Enter a number \n");
    scanf("%d", &n);
    for(i=2; i<n; i++){
        if(n%i==0){
            prime=0;
        }
    }
    if(prime==0){
        printf("this is not a prime number");
    }
    else{
        printf("this is a prime number");
    }
    return 0;
}