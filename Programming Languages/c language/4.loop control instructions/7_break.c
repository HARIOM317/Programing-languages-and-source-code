#include<stdio.h>

int main(){
    int i = 0;
    do{
        printf("the value of i is %d \n", i);
        if(i==20){
            break;
        }
        i++;
    }while(i<100);
    return 0;
}