#include<stdio.h>
#include<string.h>

struct employee{
        int code;
        float salary;
        char name[20];
    };

int main(){
    struct employee e1;
    e1.code = 101;
    e1.salary = 5000.50;
    strcpy(e1.name, "hariom");

    struct employee e2;
    e2.code = 102;
    e2.salary = 7000.56;
    strcpy(e2.name, "pooja");

    struct employee e3;
    e3.code = 103;
    e3.salary = 70056.56;
    strcpy(e3.name, "Abhishek");

    printf("\n %d\n", e1.code);
    printf("%.2f\n", e1.salary);
    printf("%s\n", e1.name);

    printf("\n*********************************************\n\n");
    printf("%d\n", e2.code);
    printf("%.2f\n", e2.salary);
    printf("%s\n\n", e2.name);
    
    printf("\n*********************************************\n\n");
    printf("%d\n", e3.code);
    printf("%.2f\n", e3.salary);
    printf("%s\n\n", e3.name);
    
    return 0;
}