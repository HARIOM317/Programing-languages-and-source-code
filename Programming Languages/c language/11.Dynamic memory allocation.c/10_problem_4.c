#include<stdio.h>
#include<stdlib.h>

int main(){
    int *ptr;
    ptr = (int*)malloc(10*sizeof(int));
    for(int i=0; i<10; i++){
        printf("7 x %d = %d \n", i+1, 7*(i+1));
    }

    printf("\n************After realloc**************\n\n");

    ptr = realloc(ptr, 15*sizeof(int));
    for(int i=0; i<15; i++){
        printf("7 x %d = %d \n", i+1, 7*(i+1));
    }
    return 0;
}