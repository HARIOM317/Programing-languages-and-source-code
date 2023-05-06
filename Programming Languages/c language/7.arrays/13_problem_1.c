#include<stdio.h>

int main(){
    int arr[10];
    // int *ptr = &arr[0];
    int *ptr = arr;
    ptr = ptr+2;
    if(ptr==&arr[2]){
        printf("these points to the same location in the memory \n");
    }
    else{
        printf("these points do not to the same location in the memory \n");
    }
    return 0;
}