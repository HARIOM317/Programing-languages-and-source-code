#include<stdio.h>

int main(){
    int a = 587;     
    int *ptr;   //this is a wild pointer.
    // *ptr = 54; //this is not a good thing to do 
    ptr = &a; //ptr is no longer a wild pointer
    printf("The value of a is %d\n", *ptr);    
    return 0;
}   