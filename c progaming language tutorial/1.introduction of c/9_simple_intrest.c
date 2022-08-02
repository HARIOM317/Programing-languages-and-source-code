#include<stdio.h>

int main(){
    int principle,rate,years;
    
    printf("enter the principle\n");
    scanf("%d", &principle);

    printf("enter the rate\n");
    scanf("%d", &rate);

    printf("enter the years\n");
    scanf("%d", &years);

    printf("the value of simple intrest is %d", (principle*rate*years)/100);

    return 0;
}