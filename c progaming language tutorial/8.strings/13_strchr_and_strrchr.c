#include<stdio.h>
#include<string.h>

int main(){
    printf("\n STRCHR() FUNCTION\n\n");
    char str[] = "Hello friends my name is hariom mewada";
    char ex = 'i';
    char *ptr = strchr(str, ex); //it works left to right.
    printf("%s \n", ptr);

    printf("\n STRRCHR() FUNCTION\n\n");
    char str2[] = "Hello friends my name is hariom mewada";
    char exe = 'i';
    char *ptr2 = strrchr(str2, exe); //it works right to left.
    printf("%s\n\n", ptr2);
    return 0;
}