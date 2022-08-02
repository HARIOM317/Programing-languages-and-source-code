#include<stdio.h>

int main(){
    int a, b ;
    int*pa, *pb;
    pa= &a;
    pb= &b;
    printf("Enter first intiger \n");
    scanf("%d", &pa);
    printf("Enter second intiger \n");
    scanf("%d", &pb);
    if(pa==pb){
        printf("Integers are equal \n");
    }
    else{
        printf("Integers are not equal \n");
    }
    return 0;
}