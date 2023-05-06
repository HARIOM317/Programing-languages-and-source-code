#include<stdio.h>

int main(){
    float n1,n2,n3,n4;
    printf("enter first number\n");
    scanf("%f", &n1); 
    printf("enter second number\n");
    scanf("%f", &n2);
    printf("enter third number\n");
    scanf("%f", &n3);
    printf("enter fourth number\n");
    scanf("%f", &n4);
    
    if(n1>=n2 && n1>=n3 && n1>=n4){
        printf("%f is the largest number\n", n1);
    }

    if(n1<=n2 && n1<=n3 && n1<=n4){
        printf("%f is the lowest number\n", n1);
    }

    if(n2>=n1 && n2>=n3 && n2>=n4){
        printf("%f is the largest number\n", n2);
    }

    if(n2<=n1 && n2<=n3 && n2<=n4){
        printf("%f is the lowest number\n", n2);
    }

    if(n3>=n1 && n3>=n2 && n3>=n4){
        printf("%f is the largest number\n", n3);
    }

     if(n3<=n1 && n3<=n2 && n3<=n4){
        printf("%f is the lowest number\n", n3);
    }

    if(n4>=n1 && n4>=n2 && n4>=n3){
        printf("%f is the largest number\n", n4);
    }

    if(n4<=n1 && n4<=n2 && n4<=n3){
        printf("%f is the lowest number\n", n4);
    }

    return 0;
}