#include<stdio.h>
#include<string.h>

int main(){
    char str1[30] = {0};
    char str2[30] = {0};
    printf("Enter string 1: ");
    gets(str1);
    strncpy(str2, str1, 3);
    printf("After copying str is : %s \n", str2);
    return 0;
}