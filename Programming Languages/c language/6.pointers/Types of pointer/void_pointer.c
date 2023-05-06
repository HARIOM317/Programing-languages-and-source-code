#include<stdio.h>

int main(){
    int a = 45;
    float b = 98.215;
    char c = 'H';
    void *ptr;
    ptr = &a;
    printf("The value of a is %d \n", *((int*)ptr));  
    ptr = &b;
    printf("The value of b is %f \n", *((float*)ptr));          //it will be print value of a because typecast is clear.
    // printf("The value of a is %d \n", *ptr);          //it will not print value of a because typecast is not clear.
    ptr = &c;        //it will be print value of a because typecast is clear.
    printf("The value of c is %c \n", *((char*)ptr));  
    return 0;
}