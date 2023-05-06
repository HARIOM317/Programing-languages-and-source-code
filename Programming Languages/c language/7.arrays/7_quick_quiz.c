#include<stdio.h>

int main(){
    printf("ADDITION OF A NUMBER TO A POINTER \n");
    int a = 5;
    int *ptr = &a;
    printf("the value of a is %u \n", ptr);
    ptr = ptr+5;
    printf("the value of a is %u \n\n", ptr);

    printf("SUBSTRACTION OF A NUMBER FROM A POINTER \n");
    int b=6;
    int *ptr2 = &b;
    printf("the value of b is %u \n", ptr2);
    ptr2 = ptr2-3;
    printf("the value of b is %u \n\n", ptr2);

    printf("SUBSTRACTION OF ONE POINTER FROM ANOTHER POINTER \n");
    int x=7,y=5,z=4;
    int *p = &x;
    int *q = &y;
    int *r = &z;
    printf("here p is %d q is %d r is %d p-q is %d q-r is %d r-p is %d \n\n",p, q, r, (p-q), (q-r), (r-p));

    printf("COMPARISION OF TWO POINTER VARIABLES \n");
    int c, d;
    int *pc = &c;
    int *pd = &d;
    printf("Enter first intiger \n");
    scanf("%d", &pc);
    printf("Enter second intiger \n");
    scanf("%d", &pd);
    if(pc==pd){
        printf("both are equal \n");
    }
    else{
        printf("both not are equal \n");
    }

    return 0;
}