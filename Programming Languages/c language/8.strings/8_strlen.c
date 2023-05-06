#include<stdio.h>
#include<conio.h>
#include<string.h>

int main(){
    char arr[1000];
    printf("Enter the charecter \n");
    gets(arr);
    int a = strlen(arr);
    printf("the leanth of %s character is %d",arr, a);
    getch();
    return 0;
}