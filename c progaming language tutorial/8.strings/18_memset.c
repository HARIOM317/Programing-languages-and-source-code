#include<stdio.h>
#include<string.h>

int main(){
    char ptr[] = "This is a example of memset() function";
    puts(ptr);
    memset(ptr+10, '$', 7);
    puts(ptr);
    return 0;
}