#include<stdio.h>

int main(){
    int i = 8;
    int *ptr = &i;
    printf("the memory address of i is %u \n", ptr);
    ptr++;
    ptr++;
    ptr = ptr+1;
    ptr = ptr+3;
    ptr++;
    ptr--;
    ptr = ptr-1;
    printf("the memory address of i is %u \n\n", ptr);

    char c = 58;
    char *ptr_2 = &c;
    printf("the memory address of c is %u \n", ptr_2);
    ptr_2++;
    ptr_2 = ptr_2+2;
    printf("the memory address of c is %u \n\n", ptr_2);

    float f = 58;
    float *ptr_3 = &f;
    printf("the memory address of f is %u \n", ptr_3);
    ptr_3++;
    ptr_3 = ptr_3-4;
    printf("the memory address of f is %u \n\n", ptr_3); 
   
    return 0;
}