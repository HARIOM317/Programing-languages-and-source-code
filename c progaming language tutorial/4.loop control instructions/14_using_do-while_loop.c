#include<stdio.h>

int main(){
    int i=2, n,prime;
    printf("Enter a number\n");
    scanf("%d", &n);
    do{
        if(n%i==0){
            prime = 0;
            break;
        }
        i++;
    }while(i<n);

    if(prime==0){
        printf("this is not a prime number\n");
    }
    else{
        printf("this is a prime number\n");
    }
    return 0;
}