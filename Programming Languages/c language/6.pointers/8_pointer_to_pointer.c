#include<stdio.h>

int main(){
    int i = 654;
    int *a = &i;
    int **b = &a;
    printf("the value of i is %d \n", **b); 
    return 0;
}