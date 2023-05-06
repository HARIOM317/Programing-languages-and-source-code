#include<stdio.h>

int main(){
    FILE *ptr;
    FILE *ptr2;
    int num;
    printf("Enter a number \n");
    scanf("%d", &num);
    ptr = fopen("number.txt", " w");
    fprintf(ptr,"%d", 2*num );
    ptr2 = fopen("number.txt", "r");
    fscanf(ptr, "%d", &num);
    printf("the value of num is: %d", num);
    return 0;
}