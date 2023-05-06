#include<stdio.h>
#include<string.h>

struct employee{
    int code;
    float salary;
    char name[20];
};
int main(){
  struct employee a1,a2,a3;
  printf("Enter the code of a1 employee : ");
  scanf("%d", &a1.code); 
  printf("Enter the salary of a1 employee : ");
  scanf("%f", &a1.salary); 
  printf("Enter the name of a1 employee : ");
  scanf("%s", a1.name);  

  printf("Enter the code of a2 employee : ");
  scanf("%d", &a2.code); 
  printf("Enter the salary of a2 employee : ");
  scanf("%f", &a2.salary); 
  printf("Enter the name of a2 employee : ");
  scanf("%s", a2.name);  

  printf("Enter the code of a3 employee : ");
  scanf("%d", &a3.code); 
  printf("Enter the salary of a3 employee : ");
  scanf("%f", &a3.salary); 
  printf("Enter the name of a3 employee : ");
  scanf("%s", a3.name);  
  printf("\n*********************************************\n\n");

  printf("The code of a1 employee is %d \n ", a1.code);
  printf("The salary of a1 employee is %.2f \n ", a1.salary);
  printf("The name of a1 employee is %s \n ", a1.name);
  printf("\n*********************************************\n\n");

  printf("The code of a2 employee is %d \n ", a2.code);
  printf("The salary of a2 employee is %.2f \n ", a2.salary);
  printf("The name of a2 employee is %s \n ", a2.name);
  printf("\n*********************************************\n\n");

  printf("The code of a3 employee is %d \n ", a3.code);
  printf("The salary of a3 employee is %.2f \n ", a3.salary);
  printf("The name of a3 employee is %s \n ", a3.name);
  printf("\n*********************************************\n\n");

 
    return 0;
}