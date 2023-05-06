#include<stdio.h>

int main(){
    int n;
    printf("enter a number \n");
    scanf("%d", &n);
    if(n%2==0){
        printf("this is a even number \n");
    }
    else{
        printf("this is a odd number");
    }

    return 0;
}