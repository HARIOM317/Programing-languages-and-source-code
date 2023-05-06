#include<stdio.h>

int main(){
    int a;
    printf("enter percentage\n");
    scanf("%d", &a);
    if(a==100){
        printf(" congratulation ! you are topper");
    }
    else if(a>=90 && a<100){
        printf("you have got A+ grade");
    }
    else if(a>=75 && a<90){
        printf("you have got A grade");
    }
    else if(a>=60 && a<75){
        printf("you have got B grade");
    }
    else if(a>=45 && a<60){
        printf("you have got C grade");
    }
    else if(a>=33 && a<45){
        printf("you have got D grade");
    }
    else if(a<33 && a>0){
        printf("you are fail");
    }
    else {
        printf("invalid percentage");
    }
    return 0;
}