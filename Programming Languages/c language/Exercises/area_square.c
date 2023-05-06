#include<stdio.h>
#include<math.h>

int main(){
    int a;
    printf("enter a side of square in cm. \n");
    scanf("%d", &a);
    printf("the area of side %d is %f cm square \n", a, pow(a,2));
    
    return 0;
}