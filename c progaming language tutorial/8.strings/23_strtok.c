#include<stdio.h>
#include<string.h>

int main(){
    char string[100] = "test,string1,test:string2:test-string3-test_string4";
    char *ptr;
    printf("string %s is split into tokens: \n ", string);
    ptr = strtok(string, ",:-_");
    while(ptr!=NULL){
    printf("%s \n",ptr);
    ptr = strtok(NULL, ",:-_");
    }
    return 0;
}