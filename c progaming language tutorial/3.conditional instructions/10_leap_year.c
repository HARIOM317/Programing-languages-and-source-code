#include<stdio.h>

int main(){
    int year;
    printf("Enter the year\n");
    scanf("%d", &year);
    if(year%4==0 && year%100==0 && year%400==0){
        printf(" according to the Gregorian calenderf (THIS IS A LEAP YEAR)\n");
    }
    else{
        printf(" according to the Gregorian calenderf (THIS IS NOT A LEAP YEAR)\n");
        }
    return 0;
}