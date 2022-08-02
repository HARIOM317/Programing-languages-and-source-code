#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(int argc, char *argv[])
{
    char *operation;
    int num1, num2;
    operation = argv[1];
    num1 = atoi(argv[2]);
    num2 = atoi(argv[3]);
    printf("operation is: %s\n", operation);
    printf("Num1 is: %d \n", num1);
    printf("Num2 is: %d \n", num2);
    if(strcmp(operation, "add")==0){
        printf("Sum = %d \n", num1+num2);
    }
    else if(strcmp(operation, "substraction")==0){
        printf("Substraction = %d \n", num1-num2);
    }
    else if(strcmp(operation, "multiply")==0){
        printf("Multiply = %d \n", num1*num2);
    }
    else if(strcmp(operation, "divide")==0){
        printf("Divide = %d \n", num1/num2);
    }
    return 0;
}
