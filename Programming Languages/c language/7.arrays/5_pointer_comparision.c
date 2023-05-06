#include<stdio.h>

int main(){
    int *ptrA;
    float *ptrB;
    ptrA = (int *)1000;
    ptrB = (int *)2000;
    if(ptrB>ptrA){
        printf("ptrB is greater than ptrA");
    }
    else{
        printf("ptrA is greater than ptrB");
    }
    return 0;
}