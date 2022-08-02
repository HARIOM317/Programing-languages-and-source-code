#include<stdio.h>

int main(){
    FILE *fptr;
    int num = 78;
    char s[50] = "hari";
    fptr = fopen("genarate.txt", "w");
    fprintf(fptr,"the value of num is: %d \n", num);
    fprintf(fptr,"Thanks for using fprintf %s\n", s);
    fprintf(fptr,"Thank you so much \n");
    fclose(fptr);

    return 0;
}