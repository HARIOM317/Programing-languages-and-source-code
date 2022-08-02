#include<stdio.h>
#include<string.h>

int main(){
    char str1[30]; 
    char str2[30];
    printf("Enter string 1: \n");
    gets(str1); 
    printf("Enter string 2: \n");
    gets(str2); 
    printf("Using strcmp: \n");
    if(strcmp(str1, str2)==0){
        printf("strings are same \n");
    }
    else{
        printf("strings are not same \n");
    }
    printf("\n Using strcmpi :\n");
    if(strcmpi(str1, str2)==0){
        printf("strings are same \n");
    }
    else{
        printf("strings are not same \n");
    }

    return 0;
}