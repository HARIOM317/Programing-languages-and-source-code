#include<stdio.h>
int occurence(char str[], char c){
    char *ptr = str;
    int count = 0;
    while(*ptr!='\0'){
        if(*ptr==c){
            count++;
        }
        ptr++;
    }
    return count;
}
int main(){
    char str[] = "hariom singh rajput";
    int count = occurence(str, 'h');
    if(count>=1){
            printf("Given Character is present in string");  
            }
            else{
                printf("Given Character is not present in string");
            }
    return 0;
}