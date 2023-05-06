#include<stdio.h>
float fahrenheit(float a);
int main(){
    int n;
    printf("Enter a value of celsius to convert into fahrenheit \n");
    scanf("%d", &n);
    printf("the value of %d degree celsius in fahrenheit is %.2f degree fahrenheit\n", n, fahrenheit(n));
    return 0;
}
float fahrenheit(float celsius){
    float result;
    result= (float)(celsius*9/5)+32;
    return result;
}