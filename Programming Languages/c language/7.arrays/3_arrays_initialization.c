#include<stdio.h>

int main(){
    int a[] = {89,97,65,54,35,75};
    printf("the value of a[0] is %d \n", a[0]);
    printf("the value of a[1] is %d \n", a[1]);
    printf("the value of a[2] is %d \n", a[2]);
    printf("the value of a[3] is %d \n", a[3]);
    printf("the value of a[4] is %d \n", a[4]);
    printf("the value of a[5] is %d \n\n", a[5]);

    float b[] = {89.54,97.35,65.32,54.36,35.54,75.98};
    printf("the value of b[0] is %.2f \n", b[0]);
    printf("the value of b[1] is %.2f \n", b[1]);
    printf("the value of b[2] is %.2f \n", b[2]);
    printf("the value of b[3] is %.2f \n", b[3]);
    printf("the value of b[4] is %.2f \n", b[4]);
    printf("the value of b[5] is %.2f \n\n", b[5]);

    char c[] = {31,125,87,54,65,89};
    printf("the value of c[0] is %c \n", c[0]);
    printf("the value of c[1] is %c \n", c[1]);
    printf("the value of c[2] is %c \n", c[2]);
    printf("the value of c[3] is %c \n", c[3]);
    printf("the value of c[4] is %c \n", c[4]);
    printf("the value of c[5] is %c \n", c[5]);
    return 0;
}