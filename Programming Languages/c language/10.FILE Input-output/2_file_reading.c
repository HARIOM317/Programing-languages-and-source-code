#include<stdio.h>

int main(){
    FILE *ptr;
    int num;
    int num2;
    ptr = fopen("hariom.txt", "r");
    fscanf(ptr, "%d", &num);
    fscanf(ptr, "%d", &num2);
    fclose(ptr);
    printf("THE value of num is: %d \n", num);
    printf("THE value of num2 is: %d \n", num2);

    return 0;
}