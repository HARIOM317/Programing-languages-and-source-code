#include<stdio.h>
#include<string.h>

int main(){
    char string[20] = "Test string";
    strset(string, '#');
    printf("%s \n", string);

    char str[20] = "Test string";
    strnset(str, '*', 4);
    printf("%s \n", str);
    return 0;
}