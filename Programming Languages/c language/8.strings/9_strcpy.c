#include<stdio.h>
#include<string.h>

int main(){
    char *st = "hariom";
    char st2[50];
    strcpy(st2, st);
    printf("Now the st2 is %s", st2);
    return 0;
}