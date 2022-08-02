#include<stdio.h>

int factorial(int n);

int main(){
    int n;
    printf("Enter a value for factorial \n");
    scanf("%d", &n);
    printf("The value of factorial %d is %d \n", n, factorial(n) );
    return 0;
}
int factorial(int x){
    printf("calling factorial (%d)\n", x);
    if(x==1 || x==0){
        return 1;
    }
    else{
        return x*factorial(x-1);
    }
}