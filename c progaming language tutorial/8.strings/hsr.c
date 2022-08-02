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
    if(count<=1){
                    printf("Occurences = %d \n", count);
            }
            else if(count>1){
            printf("occurence is present in string \n");
            }
    return 0;
}