#include<stdio.h>

int main(){
    char str[] = "HARIOM SINGH RAJPUT";
    char *ptr = str;
    while(*ptr!='\0'){
        printf("%c", *ptr);
        ptr++;
    }
    return 0;
}