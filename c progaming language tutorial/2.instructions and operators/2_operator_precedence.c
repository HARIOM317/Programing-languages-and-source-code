#include<stdio.h>

int main(){
    int x = 3;
    int y = 5;
    printf("the value of 3*x - 8*y is %d\n", 3*x - 8*y);
    printf("the value of 8*y / 3*x is %d\n", 8*y / 3*x );
    // 8*y / 3*x will give wrong answer
    // 8*5/3*3
    // 40/3*3
    // 13*3
    // 39
    printf("the value of (8*y) / (3*x) is %d\n", (8*y) / (3*x) ); 
    // it will give write answer
    
    return 0;
}