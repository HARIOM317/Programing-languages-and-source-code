#include<stdio.h>
#include<string.h>

int main(){
    char word1[50] = "don't undarestimate the power of hsr";
    char word2[50] = "power of hsr";
    if(strstr(word1, word2) != NULL){
        printf("Substring found \n");
    }
    else{
        printf("Substring not found \n");
    }
    char *ptr =strstr(word1, "the");
    printf("%s\n", ptr);

    char *ptr2 =strstr(word2, "p");
    printf("%s", ptr2);
    return 0;
}