#include<stdio.h>
#include<string.h>

int main(){
    char str[30];
    printf("enter string \n");
    gets(str);
    printf("Entered string is: %s \n", str);
    strrev(str);
    printf("reversed string is: %s\n", str);
    return 0;
}