#include<stdio.h>

int main(){
    FILE *ptr;
    int num;
    ptr = fopen("hsr.txt", "r");
    fscanf(ptr, "%d", &num);
    printf("The value of num is %d\n", num);
    int number=num*2;
    ptr = fopen("hsr.txt", "w");
    fprintf(ptr, "%d", number);
    return 0;
}