#include<stdio.h>

int main(){
    char ch;
    // ASCII value of lowercase is 97-122
    printf("Enter the charectere\n");
    scanf("%C", &ch);
    if(ch>=97 && ch<=122){
        printf("it is a lowercase\n");
    }
    else{
        printf("it is not a lowercase");
    }
    return 0;
}