#include<stdio.h>
#include<string.h>

int main(){
    char *p1 = "RAJA";
    char *p2 = strdup(p1);
    printf("Duplicate string is: %s \n", p2);
    return 0;
}