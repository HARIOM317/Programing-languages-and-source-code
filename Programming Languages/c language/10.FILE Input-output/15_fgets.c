#include<stdio.h>

int main(){
    FILE *ptr;
    ptr = fopen("fputDemo3.txt", "w");
    fputs("hariom", ptr);
    fclose(ptr);
    return 0;
}