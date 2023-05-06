#include<stdio.h>

int main(){
    // char arr[] = {'H', 'A', 'R', 'I', 'O', 'M', '\0'};
    char str[] = "HARIOM";
    char *ptr = str;
    for(int i=0; i<=5; i++){
        *ptr!='\0';
        printf("The address of %c is %u \n", *ptr, ptr);
        ptr++;
    }
    return 0;
}