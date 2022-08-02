#include<stdio.h>

int main(){
    int ch1, ch2='\n', ch3=67;
    printf("Enter a character : ");
    ch1 = fgetchar();
    printf("Enter another charactor : ");
    fflush(stdin);
    fputchar(getchar());
    putchar(ch2);
    putchar(ch1);
    putchar('\n');
    putchar(ch3);
    putchar(10);
    printf("thank you ");
    return 0;
}