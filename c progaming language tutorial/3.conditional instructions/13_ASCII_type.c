#include<stdio.h>

int main(){
    char ch;
    printf("Enter charecter,number or symbol\n");
    scanf("%c", &ch);
    if(ch>=33 && ch<=47 || ch>=58 && ch<=64 || ch>=91 && ch<=96 || ch>=123 && ch<=126){
        printf("this is special charecter or symbol\n");
    }
    if(ch>=48 && ch<=57){
        printf("this is a number\n");
    }
    if(ch>=64 && ch<=90){
        printf("this is a UPPER CASE charecter\n"); 
    }
    if(ch>=97 && ch<=122){
        printf("this is a lower case charecter");
    }
    return 0;
}