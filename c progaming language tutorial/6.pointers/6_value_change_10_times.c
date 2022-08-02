#include<stdio.h>
void pass(int *a);
int main(){
    int i;
    printf("Enter the number \n");
    scanf("%d", &i);
    pass(&i);
    printf("required value of i is %d \n", i);

    return 0;
}
void pass(int *a){
    int temp = *a;
    *a= 10*temp;
}