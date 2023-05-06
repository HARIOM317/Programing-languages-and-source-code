#include<stdio.h>
#include<stdlib.h>
// int* functionDangling(){
//     int a, b, sum;
//     a = 5448;
//     b = 788;
//     sum = a+b;
//     return &sum;
// }
int main(){
    //case 1 : De allocation of a memory
    // int *ptr = (int*)malloc(7*sizeof(int));
    // ptr[0] = 45;
    // ptr[1] = 4525;
    // ptr[2] = 455;
    // ptr[3] = 785;
    // free(ptr); //ptr is now a dangling pointer 

    //case 2 : FUNCTION RETURNING LOCAL VARIABLE ADDRESS.
    // int* dangptr = functionDangling();    //dangptr is now a dangling pointer

    // // case 3 : if a variable goes out of scope.
    int * danglingptr3;
    {
        int a = 5;
        danglingptr3 = &a;
    }
    // here variable a goes out of scope which means danglingptr3 is pointing to a location which is freed and hence danglingptr3 is now a dangling pointer.
    return 0;
}