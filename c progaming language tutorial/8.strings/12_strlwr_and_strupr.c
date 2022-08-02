#include<stdio.h>
#include<string.h>

int main(){
    char str[20];
    printf("Enter string \n");
    gets(str);
    printf("string is %s \n", str);
    printf("lower string is %s \n", strlwr(str));
    printf("upper string is %s \n", strupr(str));

    return 0;
}