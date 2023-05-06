#include<stdio.h>

int main(){
    FILE *ptr;
    ptr = fopen("fputDemo.txt2", "w");
    fputc('H', ptr);
    fputc('A', ptr);
    fputc('R', ptr);
    fputc('I', ptr);
    fputc('O', ptr);
    fputc('M', ptr);
    fputc(' ', ptr);
    fputc('R', ptr);
    fputc('A', ptr);
    fputc('J', ptr);
    fputc('P', ptr);
    fputc('U', ptr);
    fputc('T', ptr);


    fclose(ptr);
    return 0;
}