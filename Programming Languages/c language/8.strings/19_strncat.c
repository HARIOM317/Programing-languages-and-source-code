#include<stdio.h>
#include<string.h>

int main(){
    char source[] = "fresh 2 fresh";
    char target[] = "c tutorial";
    printf("\n source string = %s", source);
    printf("\n target string = %s \n", target);
    strncat(target, source, 5);
    printf("target string after strncat() = %s ", target);
    
    return 0;
}