#include<stdio.h>
void address(int a){
    printf("The address of i is %u \n", &a);
}
int main(){
    int i = 5;
    printf("The value of i is %d \n", i);
    printf("The address of i is %u \n", &i);
    address(i);
    return 0;
} 