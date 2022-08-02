#include<stdio.h>
void pass(int a){
    int result=a;
    a=10*result;
}
int main(){
    int i =6;
    pass(i);
    printf("the required value is %d\n", i);
    return 0;
}