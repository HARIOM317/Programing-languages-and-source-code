#include<stdio.h>

int main(){
    char hsr[100];
    char hsr2[100];
    printf("Enter your name: ");
    gets( hsr);
    printf("where do you live: ");
    gets(hsr2);
    printf("\n\nYour name is %s \n\n", hsr);
    printf("You live in %s \n", hsr2);
    printf("\n*************************x***************************X************************x*********************** \n\n");
    return 0;
}