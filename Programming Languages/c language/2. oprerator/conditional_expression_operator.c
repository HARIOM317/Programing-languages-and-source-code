#include<stdio.h>

int main(){
    int age;
    printf("Enter your age: \n");
    scanf("%d", &age);
    int a = age<18? 100:200;
    printf("%d\n", a);
    
    return 0;
}