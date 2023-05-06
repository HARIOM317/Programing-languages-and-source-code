#include<stdio.h>
#include<string.h>

int main(){
    char s1[20] = "Hello ";
    // char s2[] = "hariom";
    char *s2 = "Hariom";
    strcat(s1,s2);
    printf("Now the s1 is %s", s1);
    return 0;
}