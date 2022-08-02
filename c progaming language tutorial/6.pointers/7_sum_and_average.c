#include<stdio.h>
void Sum_And_Avg(int a, int b, int*sum, float*avg);
int main(){
    int i , j;
    printf("Enter first number \n");
    scanf("%d", &i);
     printf("Enter second number \n");
    scanf("%d", &j);
    int sum;
    float avg;
    Sum_And_Avg(i, j, &sum, &avg);
    printf("The sum is %d \n", sum);
    printf("The avg is %.2f \n", avg);
    return 0;
}
void Sum_And_Avg(int a, int b, int*sum, float*avg){
    *sum = a+b;
    *avg = (float)(*sum)/2;
}
