#include<stdio.h>

int main(){
    int A=70;
    int B=15;
    printf("Bitwise operator returns %d \n", A&B);
    printf("Bitwise operator returns %d \n", A|B);
    printf("Bitwise operator returns %d \n", A^B);
    printf("Bitwise operator returns %d \n", ~A);
    printf("Bitwise operator returns %d \n", ~B);
    printf("Bitwise operator returns %d \n", A<<B);
    printf("Bitwise operator returns %d \n", A>>B);
    return 0;
}