#include<stdio.h>
int main(){
    int a=8;
    int *b = &a;
    printf("the value of a is %u \n", *b);
    printf("the address of a is %u \n", b);
    return 0;
}



