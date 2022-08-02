#include<stdio.h>
// void printarray(int *ptr, int a){
//     for( int i=0; i<5; i++){
//     printf("the value of element %d is %d\n", i+1, *(ptr+i));
//     }
    void printarray(int ptr[], int a){                          //BOTH ARE RIGHT
    for( int i=0; i<5; i++){
    printf("the value of element %d is %d\n", i+1, ptr[i]);
    }
    ptr[2] =888889;         //this value will be change in main function.
}
int main(){
    int arr[] = {54,65,87,65,49};
    printarray(arr,5);
    printf("the 87 will be change in to %d", arr[2]);
    return 0;
}