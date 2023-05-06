#include<stdio.h>
#include<string.h>

struct employee{
    int code;
    float salary;
    char name[30];
};

void show(struct employee emp){
    printf("The code of employee is: %d \n", emp.code);
    printf("The salary of employee is: %f \n", emp.salary);
    printf("The name of employee is: %s \n", emp.name);
    emp.code = 102;     //it will be not change because only value will be copy not update.

}
int main(){
    struct employee e1;
    struct employee *ptr;
    ptr = &e1;
    ptr->code = 101;
    ptr->salary = 10000;
    strcpy(ptr->name, "hariom");
    
    show(e1);
    printf("Now the code of employee is : %d \n", e1.code);         //so...It will be not print.
    return 0;
}