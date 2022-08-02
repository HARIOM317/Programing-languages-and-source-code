#include<stdio.h>

int main(){
    int size;
    int arr[100];
    int positive = 0, negative =0;
    printf("\n please enter the size of an Array: \n");
    scanf("%d", &size);

    printf("Please enter the array element \n");
    for(int i=0; i<size; i++){
        scanf("%d", &arr[i]);
    }

    for(int i=0; i<size; i++){
        if(arr[i]>=0){
            positive++;
        }
        else{
            negative++;
        }
    }
    printf("\n total positive number = %d", positive);
    printf("\n total negative number = %d", negative);
    return 0;
}