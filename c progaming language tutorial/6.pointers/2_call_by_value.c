#include<stdio.h>
int sum(int a, int b);
int main(){
    int a =5, b=8;
    printf("the value of a and b is %d and %d \n", a, b);
    printf("the sum of a and b is %d \n", sum(a,b));
    printf("the value of a and b after function call is %d and %d \n", a, b);
    return 0;
}
int sum(int a, int b){
   int c= a+b;
    a =545;
    b= 845;
    return c;
}