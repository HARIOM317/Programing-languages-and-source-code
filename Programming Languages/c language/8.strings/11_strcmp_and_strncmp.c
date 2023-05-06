#include<stdio.h>
#include<string.h>

int main(){
    char A[20] = "New york";
    char B[20] = "New delhi";
    int val = strcmp(A,B);
    if(val==0){
        printf("Both strings are equal\n\n");
    }
    else if(val>0){
        printf("\nstring A is greather than string B \n\n");
    }
    else{
        printf("string B is greather than string A \n");
    }
    printf("\n******************************************************\n\n");

    int val2 = strncmp(A,B,3);
    if(val2==0){
        printf("Both strings are equal\n\n");
    }
    else if(val2>0){
        printf("string A is greather than string B \n\n");
    }
    else{
        printf("string B is greather than string A \n\n");
    }
    return 0;
}