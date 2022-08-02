#include<stdio.h>

int main(){
    char *ptr ="hariom rajput";
    // char ptr[] = "hariom rajput";  //cannot be reinitialized.
    ptr = "hariom singh rajput";
    ptr = "HSR";
    printf("%s",ptr);
    return 0;
}