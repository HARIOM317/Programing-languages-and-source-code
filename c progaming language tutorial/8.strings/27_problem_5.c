#include<stdio.h>

int strcpy(char *str, char *str2, char c){
char *ptr = str;
char *ptr2 = str2;
char len = 0;
while(*ptr!='\0'){
    len++;        
    ptr++;
    }
return len;
}

int main(){
    char str[] = "hariom";
    char str2[50];
    strcpy(str2, str);
    printf("the length of this string is %s", str2);
    return 0;
}