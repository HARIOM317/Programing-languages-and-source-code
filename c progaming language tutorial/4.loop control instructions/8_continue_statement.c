#include<stdio.h>

int main(){
    int skip=10, i=0;
    while(i<100){
        i++;
        if(i!= skip){
            continue;
        }
        else{
            printf("%d\n", i);
        }
    }
    return 0;
}