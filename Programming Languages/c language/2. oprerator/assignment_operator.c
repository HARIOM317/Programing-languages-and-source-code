#include<stdio.h>

int main(){
    int a = 25;
    a+=25;
    printf("a is: %d\n", a);
    a-=25;
    printf("a is: %d\n", a);
    a*=25;
    printf("a is: %d\n", a);
    a/=20;
    printf("a is: %d\n", a);
    a%=2;
    printf("a is: %d\n", a);
    a<<=2;
    printf("a is: %d\n", a);
    a>>=2;
    printf("a is: %d\n", a);
    a&=2;
    printf("a is: %d\n", a);
    a^=2;
    printf("a is: %d\n", a);
    a|=2;
    printf("a is: %d\n", a);

    return 0;
}